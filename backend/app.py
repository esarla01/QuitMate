from config import Config 
from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from pymongo import MongoClient
from chat_utils import generate_response
from flask_cors import cross_origin
import uuid

app = Flask(__name__)
CORS(app) 

client = MongoClient(Config.MONGO_URI)
db = client["chatbot_db"]  
chats_collection = db["chats"]  

@app.route('/chats/user/<user_id>', methods=['GET'])
def get_or_create_chat(user_id):
    chat = chats_collection.find_one({"user_id": user_id})

    if chat:
        return jsonify({"chat_id": chat["chat_id"]}) 

    chat_id = str(uuid.uuid4())
    chat_data = {"user_id": user_id, "chat_id": chat_id, "messages": []}
    chats_collection.insert_one(chat_data)

    return jsonify({"chat_id": chat_id})  


@app.route('/chats', methods=['POST'])
def create_chat():
    user_id = request.json.get("user_id")

    if not user_id:
        return jsonify({"error": "User ID is required"}), 400

    existing_chat = chats_collection.find_one({"user_id": user_id})

    if existing_chat:
        return jsonify({"id": existing_chat["chat_id"]})  

    chat_id = str(uuid.uuid4())
    chat_data = {"user_id": user_id, "chat_id": chat_id, "messages": []}
    chats_collection.insert_one(chat_data)


    return jsonify({"id": chat_id})

@app.route('/chats/<chat_id>', methods=['POST'])
def send_message(chat_id):
    chat_data = chats_collection.find_one({"chat_id": chat_id})

    if not chat_data:
        return jsonify({"error": "Chat session not found"}), 404

    user_message = request.json.get("message", "").strip()
    if not user_message:
        return jsonify({"error": "Message cannot be empty"}), 400

    chat_data["messages"].append({"role": "user", "content": user_message})

    def generate():
        for chunk in generate_response(chat_data["messages"], user_message):
            yield f"data: {chunk}\n\n"

        assistant_message = "".join(generate_response(chat_data["messages"], user_message))
        chat_data["messages"].append({"role": "assistant", "content": assistant_message})

        chats_collection.update_one({"chat_id": chat_id}, {"$set": {"messages": chat_data["messages"]}})

    return Response(generate(), content_type="text/event-stream")

@app.route('/chats/<chat_id>/messages', methods=['GET'])
def get_chat(chat_id):
    chat_data = chats_collection.find_one({"chat_id": chat_id})

    if not chat_data:
        return jsonify({"error": "Chat session not found"}), 404

    return jsonify(chat_data["messages"])

@app.route('/')
def home():
    return "Welcome to the home page!"


if __name__ == '__main__':
    app.run(debug=True)

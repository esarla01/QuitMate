# QuitMate
QuitMate is a chatbot-powered personal support system designed to assist individuals in quitting smoking. 
**QuitMate** is an AI-powered chatbot designed to assist individuals in quitting smoking by providing personalized support, motivation, and habit-tracking. This project leverages real-time AI-driven interactions to offer guidance and resources in an accessible and engaging manner.

---

## **Key Features**
- **Conversational AI**: An interactive chatbot that offers guidance, motivation, and coping strategies tailored for smoking cessation.
- **Persistent Chat History**: Retains past conversations to ensure continuity and personalization in support.
- **Real-time Message Processing**: Implements server-sent events (SSE) for seamless and dynamic responses.
- **User Authentication & Session Management**: Stores chat sessions using unique IDs for retrieval and continuity.
- **Modern UX/UI**: A responsive, user-friendly interface built for accessibility and engagement.

---

## **Tech Stack**
- **Frontend**: React.js with Tailwind CSS for a clean, modern user interface.
- **Backend**: Flask API handling chat interactions and AI-driven responses.
- **Database**: PostgreSQL (or similar) to store user conversations and session data.
- **Hosting & Deployment**: AWS (S3 for frontend, Lambda for backend functions) for scalability and efficiency.

---

## **How Modifying the Chat Utils Prompt Can Adapt the Project**
The core behavior of QuitMate is determined by the AI prompt configured in the chat utilities file. By modifying this prompt, the chatbot can be transformed for various applications, such as:

- **Mental Health Support**: Adjusting responses to provide stress management, mindfulness, and emotional support.
- **Productivity Coach**: Offering time management techniques, habit formation tips, and motivation strategies.
- **Educational AI Tutor**: Assisting users in learning languages, mathematics, or coding with interactive explanations.
- **Healthcare Assistant**: Providing symptom checks, wellness recommendations, and general medical guidance.

By simply tweaking the AI’s instructional prompt, QuitMate can be repurposed into a versatile AI-driven assistant tailored to different needs.

---

## **Project Structure**
This project consists of a **frontend** and **backend**:
- The **frontend** (React.js) provides a responsive user interface for engaging with the chatbot.
- The **backend** (Flask) manages API requests, chat session storage, and AI-driven message processing.

---

## **Setup Instructions**

### **Frontend Setup**
1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-repo/quitmate.git
   cd quitmate/frontend
   ```
2. **Install dependencies:**
   ```sh
   npm install
   ```
3. **Set up environment variables:**
   - Rename `.env-example` to `.env` in the `frontend` folder.
   - Open `.env` and configure the API URLs:
     ```sh
     REACT_APP_API_URL=http://localhost:5000
     ```
4. **Run the development server:**
   ```sh
   npm run dev
   ```
5. **Access the application:**
   Open `http://localhost:3000` in your browser.

---

### **Backend Setup**
1. **Navigate to the backend folder:**
   ```sh
   cd ../backend
   ```
2. **Create and activate a virtual environment:**
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
4. **Run the Flask server:**
   ```sh
   flask run --host=0.0.0.0 --port=5000
   ```
5. **Verify the API is running:**
   Open `http://localhost:5000` in your browser or test endpoints using Postman.

Now your QuitMate application is fully set up and ready to use!

const BASE_URL = import.meta.env.BASE_URL;


// Helper function to get or create a unique user ID
function getUserId() {
  let userId = localStorage.getItem("userId");
  if (!userId) {
    userId = crypto.randomUUID();  // Generate a unique ID
    localStorage.setItem("userId", userId);
  }
  return userId;
}

// Create or fetch an existing chat for the user
async function createChat() {
  const userId = getUserId(); // Get unique user identifier

  // Check if a chat already exists for this user
  const res = await fetch(`${BASE_URL}/chats/user/${userId}`);
  const data = await res.json();

  if (res.ok && data.chat_id) {
    return { id: data.chat_id }; // Return existing chat ID
  }

  // If no chat exists, create a new one for the user
  const createRes = await fetch(BASE_URL + '/chats', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ user_id: userId })  // Pass user ID
  });

  const createData = await createRes.json();
  if (!createRes.ok) {
    return Promise.reject({ status: createRes.status, data: createData });
  }

  return createData;
}

// Send a message to the chat
async function sendChatMessage(chatId, message) {
  const res = await fetch(BASE_URL + `/chats/${chatId}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ message })
  });

  if (!res.ok) {
    return Promise.reject({ status: res.status, data: await res.json() });
  }

  return res.body;
}


// Fetch messages for a given chatId
async function getChatMessages(chatId) {
  const res = await fetch(`${BASE_URL}/chats/${chatId}/messages`, {
    method: 'GET',
    headers: { 'Content-Type': 'application/json' },
  });

  if (!res.ok) {
    return Promise.reject({ status: res.status, data: await res.json() });
  }

  return await res.json();  // ✅ Return messages as JSON
}

export default {
  createChat,
  sendChatMessage,
  getChatMessages  

};

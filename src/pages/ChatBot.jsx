// ChatBot.jsx
import React, { useState } from "react";
import axios from "axios";

function ChatBot() {
  const [messages, setMessages] = useState([]);
  const [userInput, setUserInput] = useState("");

  const handleSendMessage = async () => {
    if (!userInput.trim()) return;

    // Add the user's message to the conversation
    const userMessage = { sender: "user", text: userInput };
    setMessages((prev) => [...prev, userMessage]);

    try {
      // Send the message to the server
      const response = await axios.post("http://localhost:5000/chat", { message: userInput });
      const botMessage = { sender: "bot", text: response.data.response };
      setMessages((prev) => [...prev, botMessage]);
    } catch (error) {
      console.error("Error communicating with server:", error);
      const errorMessage = { sender: "bot", text: "Error connecting to the server. Please try again later." };
      setMessages((prev) => [...prev, errorMessage]);
    }

    setUserInput(""); // Clear input field
  };

  return (
    <div className="chatbot-container">
      <div className="chatbox">
        {messages.map((msg, index) => (
          <div key={index} className={`message ${msg.sender}`}>
            {msg.text}
          </div>
        ))}
      </div>

      <div className="input-area">
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          placeholder="Ask a health-related question..."
        />
        <button onClick={handleSendMessage}>Send</button>
      </div>

      <style jsx>{`
        .chatbot-container {
          width: 400px;
          margin: auto;
          border: 2px solid #ccc;
          border-radius: 10px;
          padding: 10px;
        }

        .chatbox {
          max-height: 300px;
          overflow-y: auto;
          margin-bottom: 10px;
        }

        .message {
          padding: 8px 12px;
          border-radius: 10px;
          margin: 5px 0;
        }

        .message.user {
          text-align: right;
          background-color: #007bff;
          color: white;
        }

        .message.bot {
          text-align: left;
          background-color: #f1f1f1;
          color: black;
        }

        .input-area {
          display: flex;
          justify-content: space-between;
        }

        input {
          flex-grow: 1;
          padding: 10px;
          border: 1px solid #ccc;
          border-radius: 5px;
          margin-right: 10px;
        }

        button {
          padding: 10px 20px;
          border: none;
          border-radius: 5px;
          background-color: #007bff;
          color: white;
          cursor: pointer;
        }

        button:hover {
          background-color: #0056b3;
        }
      `}</style>
    </div>
  );
}

export default ChatBot;

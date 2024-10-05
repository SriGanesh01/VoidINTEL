import { useState } from 'react';

function ChatBot() {
    const [message, setMessage] = useState("");
    const [response, setResponse] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();

        const res = await fetch('http://localhost:5000/api/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ question: message })
        });

        const data = await res.json();
        setResponse(data.response);
    };

    return (
        <div>
            <h1>Medical Myths ChatBot</h1>
            <form onSubmit={handleSubmit}>
                <input
                    type="text"
                    value={message}
                    onChange={(e) => setMessage(e.target.value)}
                    placeholder="Ask a question about medical myths..."
                />
                <button type="submit">Submit</button>
            </form>
            {response && <p>Response: {response}</p>}
        </div>
    );
}

export default ChatBot;

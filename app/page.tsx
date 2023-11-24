'use client';
import React, { useEffect, useState } from 'react';
import Pusher from 'pusher-js';

export default function Home() {
  const [messages, setMessages] = useState<string[]>([]);
  const [inputMessage, setInputMessage] = useState('');

  useEffect(() => {
    const pusher = new Pusher('54b9980aed66a1f270b8', {
      cluster: 'us3',
    });

    const channel = pusher.subscribe('my-channel');

    channel.bind('my-event', function (data: any) {
      console.log('Pusher message received:', data.message);
      setMessages((prevMessages) => [...prevMessages, data.message]);
    });

    return () => {
      pusher.unsubscribe('my-channel');
      pusher.disconnect();
    };
  }, []);

  const sendMessage = () => {
    // Enviar el mensaje al servidor a través de la ruta FastAPI "/send_message"
    fetch('http://localhost:8000/send_message', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ message: inputMessage }),
    });

    // Limpiar el campo de entrada después de enviar el mensaje
    setInputMessage('');
  };

  return (
    <div className="flex flex-col items-center justify-center p-24">
      <div className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100">
        <h2 className={`mb-3 text-2xl font-semibold`}>Chat</h2>
        <div className="flex flex-col max-w-[30ch] text-sm">
          <div
            className="mb-2 overflow-auto max-h-40"
            style={{ borderBottom: '1px solid #ccc' }}
          >
            {messages.map((message, index) => (
              <div key={index}>{message}</div>
            ))}
          </div>
          <input
            type="text"
            placeholder="Type your message..."
            value={inputMessage}
            onChange={(e) => setInputMessage(e.target.value)}
            className="border border-gray-300 p-2"
          />
          <button
            onClick={sendMessage}
            className="mt-2 bg-blue-500 text-white px-4 py-2 rounded"
          >
            Send
          </button>
        </div>
      </div>
    </div>
  );
}

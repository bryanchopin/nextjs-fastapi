'use client';
import Image from "next/image";
import Link from "next/link";
import { useEffect, useState } from "react";

export default function Home() {
  const [messages, setMessages] = useState<string[]>([]);
  const [inputMessage, setInputMessage] = useState('');

  // useEffect(() => {
  //   const socket = new WebSocket("ws://localhost:8000/ws");

  //   socket.onmessage = (event) => {
  //     const receivedMessage = event.data;
  //     setMessages((prevMessages) => [...prevMessages, receivedMessage]);
  //   };

  //   socket.onclose = (event) => {
  //     console.log("Conexión WebSocket cerrada:", event);
  //   };

  //   // Limpiar la conexión WebSocket cuando el componente se desmonta
  //   return () => {
  //     socket.close();
  //   };
  // }, []);

  useEffect(() => {
    const socket = new WebSocket("ws://localhost:8000/ws");

    // Manejar eventos
    socket.onopen = (event) => {
      console.log("Conexión WebSocket abierta:", event);
    };

    socket.onmessage = (event) => {
      const receivedMessage = event.data;
      setMessages((prevMessages) => [...prevMessages, receivedMessage]);
    };

    socket.onclose = (event) => {
      console.log("Conexión WebSocket cerrada:", event);
    };

    // Limpiar la conexión WebSocket cuando el componente se desmonta
    return () => {
      socket.close();
    };
  }, []);
  const sendMessage = () => {
    const socket = new WebSocket("ws://localhost:8000/ws");

    // Esperar a que la conexión esté abierta antes de enviar el mensaje
    socket.onopen = () => {
      socket.send(inputMessage);
      setInputMessage('');
    };

    // Manejar eventos adicionales si es necesario
    socket.onclose = (event) => {
      console.log("Conexión WebSocket cerrada:", event);
    };
  };
  

  return (
    <div className="flex flex-col items-center justify-center p-24">
      <div className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100">
        <h2 className={`mb-3 text-2xl font-semibold`}>Chat</h2>
        <div className="flex flex-col max-w-[30ch] text-sm">
          <div
            className="mb-2 overflow-auto max-h-40"
            style={{ borderBottom: "1px solid #ccc" }}
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

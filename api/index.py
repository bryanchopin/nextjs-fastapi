# from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
# from fastapi.middleware.cors import CORSMiddleware
# from pusher import Pusher

# app = FastAPI()

# # Configura CORS para permitir solicitudes desde todos los orígenes
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["https://nextjs-fastapi-amber.vercel.app"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Configura las credenciales de Pusher
# pusher_client = Pusher(
#     app_id='1713056',
#     key='54b9980aed66a1f270b8',
#     secret='ea8862abeaf2572fb16c',
#     cluster='us3',
#     ssl=True
# )

# # Lista para almacenar conexiones WebSocket activas
# websocket_connections = set()

# @app.post("/send_message")
# async def send_message(message: dict):
#     # Asegúrate de que el mensaje tenga la propiedad correcta
#     if "message" not in message:
#         raise HTTPException(status_code=422, detail="Invalid message format")
    
#     # Retransmite el mensaje a todos los clientes a través de Pusher
#     pusher_client.trigger('my-channel', 'my-event', {'message': message["message"]})
#     return {"message": "Sent successfully"}

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     websocket_connections.add(websocket)

#     try:
#         while True:
#             # Puedes ignorar los mensajes entrantes en el WebSocket si no los necesitas
#             await websocket.receive_text()

#     except WebSocketDisconnect:
#         # Elimina la conexión si se desconecta
#         websocket_connections.remove(websocket)


from fastapi import FastAPI, HTTPException, WebSocket, WebSocketDisconnect
from pusher import Pusher
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configura CORS para permitir solicitudes desde todos los orígenes
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configura las credenciales de Pusher
pusher_client = Pusher(
    app_id='1713056',
    key='54b9980aed66a1f270b8',
    secret='ea8862abeaf2572fb16c',
    cluster='us3',
    ssl=True
)

# Lista para almacenar conexiones WebSocket activas
websocket_connections = set()

@app.post("/send_message", status_code=200)
async def send_message(message: dict):
    # Asegúrate de que el mensaje tenga la propiedad correcta
    if "message" not in message:
        raise HTTPException(status_code=422, detail="Invalid message format")

    # Retransmite el mensaje a todos los clientes a través de Pusher
    pusher_client.trigger('my-channel', 'my-event', {'message': message["message"]})
    return {"message": "Sent successfully"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_connections.add(websocket)

    try:
        while True:
            # Puedes ignorar los mensajes entrantes en el WebSocket si no los necesitas
            await websocket.receive_text()

    except WebSocketDisconnect:
        # Elimina la conexión si se desconecta
        websocket_connections.remove(websocket)

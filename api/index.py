# from fastapi import FastAPI, WebSocket, WebSocketDisconnect
# from pusher import Pusher

# app = FastAPI()

# # Configura las credenciales de Pusher
# pusher_client = pusher.Pusher(
#   app_id='1713056',
#   key='54b9980aed66a1f270b8',
#   secret='ea8862abeaf2572fb16c',
#   cluster='us3',
#   ssl=True
# )

# # Lista para almacenar conexiones WebSocket activas
# websocket_connections = set()

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     websocket_connections.add(websocket)

#     try:
#         while True:
#             data = await websocket.receive_text()

#             # Retransmitir el mensaje a todos los clientes a través de Pusher
#             pusher.trigger('my-channel', 'my-event', {'message': data})

#     except WebSocketDisconnect:
#         # Eliminar la conexión si se desconecta
#         websocket_connections.remove(websocket)



from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pusher import Pusher

app = FastAPI()

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

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_connections.add(websocket)

    try:
        while True:
            data = await websocket.receive_text()

            # Retransmitir el mensaje a todos los clientes a través de Pusher
            pusher_client.trigger('my-channel', 'client-my-event', {'message': data})

    except WebSocketDisconnect:
        # Eliminar la conexión si se desconecta
        websocket_connections.remove(websocket)

# from fastapi import FastAPI, WebSocket,WebSocketDisconnect

# app = FastAPI()

# @app.get("/api/python")
# def hello_world():
#     return {"message": "Hello World"}


# # @app.websocket("/ws")
# # async def websocket_endpoint(websocket: WebSocket):
# #     await websocket.accept()
    
# #     # Obtener información sobre el cliente conectado
# #     client_info = f"Client connected: {websocket.client.host}:{websocket.client.port}"
# #     await websocket.send_text(client_info)

# #     while True:
# #         data = await websocket.receive_text()
# #         await websocket.send_text(f"Message text was: {data}")


# # Lista para almacenar conexiones WebSocket activas
# websocket_connections = []

# # Ruta para manejar conexiones WebSocket

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     websocket_connections.append(websocket)

#     try:
#         while True:
#             data = await websocket.receive_text()

#             # Retransmitir el mensaje a todos los clientes conectados
#             for connection in websocket_connections:
#                 await connection.send_text(f"Cliente {websocket.client.host}: {data}")

#     except WebSocketDisconnect:
#         # Eliminar la conexión si se desconecta
#         websocket_connections.remove(websocket)



from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import Set
import pusher


app = FastAPI()

# Conjunto para almacenar conexiones WebSocket activas
websocket_connections: Set[WebSocket] = set()

pusher_client = pusher.Pusher(
  app_id='1713056',
  key='54b9980aed66a1f270b8',
  secret='ea8862abeaf2572fb16c',
  cluster='us3',
  ssl=True
)

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

# @app.websocket("/ws")
# async def websocket_endpoint(websocket: WebSocket):
#     await websocket.accept()
#     websocket_connections.add(websocket)

#     try:
#         while True:
#             data = await websocket.receive_text()

#             # Retransmitir el mensaje a todos los clientes conectados
#             for connection in websocket_connections:
#                 await connection.send_text(f"Cliente {websocket.client.host}: {data}")

#     except WebSocketDisconnect:
#         # Eliminar la conexión si se desconecta
#         websocket_connections.remove(websocket)


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            data = await websocket.receive_text()
            pusher.trigger('my-channel', 'my-event', {'message': data})

    except WebSocketDisconnect:
        pass
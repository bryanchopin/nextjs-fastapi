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

app = FastAPI()

# Conjunto para almacenar conexiones WebSocket activas
websocket_connections: Set[WebSocket] = set()

@app.get("/api/python")
def hello_world():
    return {"message": "Hello World"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    websocket_connections.add(websocket)

    try:
        while True:
            data = await websocket.receive_text()

            # Retransmitir el mensaje a todos los clientes conectados
            for connection in websocket_connections:
                await connection.send_text(f"Cliente {websocket.client.host}: {data}")

    except WebSocketDisconnect:
        # Eliminar la conexión si se desconecta
        websocket_connections.remove(websocket)

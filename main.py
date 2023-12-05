import asyncio
import threading

from websockets.server import serve

HOST = "localhost"
PORT = 8000
CHATS = []
SOCKETS = []
SERVER_SOCKET: None


async def echo(websocket):
    SOCKETS.append(websocket)
    await websocket.send("Hello From server !")
    async for message in websocket:
        if websocket is not None:
            #getMessage = await websocket.recv()
            #print(getMessage)
            print(message)
            for socket in SOCKETS:
                await socket.send(message)



async def main():
    print(f"Server started at {HOST} on {PORT} ")
    async with serve(echo, HOST, PORT):
        await asyncio.Future()  # run forever


def print_():
    print(len(SOCKETS))


asyncio.run(main())



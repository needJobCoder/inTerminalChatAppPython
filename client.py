import asyncio
import threading
import time

from websockets.sync.client import connect
import keyboard

HOST = "localhost"
PORT = 8000
SERVER = None
GOT_SERVER = False


async def send_data():
    global SERVER
    with connect(f"ws://{HOST}:{PORT}") as websocket:
        while True:
            getmessage = websocket.recv()
            SERVER = websocket
            print(getmessage)


async def record_key(websocket):
    global GOT_SERVER
    if websocket is None:
        print("Server is None")
        return
    GOT_SERVER = True
    message = input("enter message")
    websocket.send(f"{message} {time.time()}")
    await record_key(websocket)


def server_loop():
    server_loop_ = asyncio.new_event_loop()
    server_loop_.create_task(send_data())
    server_loop_.run_forever()


threading.Thread(target=server_loop).start()
if not GOT_SERVER:
    time.sleep(3)

asyncio.run(record_key(SERVER))
# record_key(SERVER)
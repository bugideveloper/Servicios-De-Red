import asyncio
import websockets
import pickle
import random
from client_methods import *



async def hello():
    uri = "ws://127.0.0.1:5678"
    async with websockets.connect(uri) as websocket:
        while True:
            archivos = get_archivos("127.0.0.1",".")
            lista = pickle.dumps(archivos)
            await websocket.send(lista)
            await asyncio.sleep(random.random() * 5)
            await websocket.recv()

asyncio.get_event_loop().run_until_complete(hello())
import asyncio
import datetime
import random
import websockets
import pickle
from client_methods import *

class SocketServer(object):
    def __init__(self):
        self.mensaje = list()
        
    async def time(self,websocket, path):
        while True:
            print("Buscando archivos")
            if self.mensaje is not None:
                for archivo in self.mensaje:
                    await websocket.send(archivo)
                await asyncio.sleep(random.random() * 5)
            #archivos = get_archivos("127.0.0.1",".")
            #for archivo in archivos:
                #await websocket.send(self.mensaje) 
            #    await websocket.send(archivo)    
            #await asyncio.sleep(random.random() * 3)
    
    async def echo(self,websocket, path):
        print("Printing an echo request")
        async for message in websocket:
            #print("Message "+message)
            #print(type(message))
            #print("Messaje "+str(message))
            
            archivos = pickle.loads(message)
            print(archivos)
            print("Messaje "+str(archivos))
            print(type(archivos))
            self.mensaje = archivos
    
    async def handler(self,websocket, path):
        consumer_task = asyncio.ensure_future(
            self.echo(websocket, path))
        producer_task = asyncio.ensure_future(
            self.time(websocket, path))
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()
    
    def start_all(self):
        start_server = websockets.serve(self.handler, "127.0.0.1", 5678)
        asyncio.get_event_loop().run_until_complete(start_server)
        asyncio.get_event_loop().run_forever()


server = SocketServer()
server.start_all()
#start_all()


"""
import asyncio
import datetime
import random
import websockets
from client_methods import *

async def time(websocket, path):
    while True:

        print("Buscando archivos")
        archivos = get_archivos("127.0.0.1",".")
        for archivo in archivos:
            await websocket.send(archivo)
        await asyncio.sleep(random.random() * 5)

start_server = websockets.serve(time, "127.0.0.1", 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()


"""


"""
import asyncio
import websockets



start_server = websockets.serve(echo, "127.0.0.1", 8765)
print("starting the server")

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

"""
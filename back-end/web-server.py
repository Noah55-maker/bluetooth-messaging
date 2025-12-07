import asyncio
from websockets.asyncio.server import serve

async def toLocal(message):
    await my_socket.send(message)

async def fromLocal(message):
    print(message)
    pass

async def handle(websocket):
    global my_socket
    my_socket = websocket

    async for message in websocket:
        await fromLocal(message)

async def main():
    async with serve(handle, "localhost", 10000):
        await asyncio.Future()

asyncio.run(main())

import asyncio
from websockets.asyncio.server import serve

sockets = set()

async def echo(websocket):
    sockets.add(websocket)

    async for message in websocket:
        toRemove = []
        for socket in sockets:
            # check for clos{ing, ed} sockets
            if socket.state == 2 or socket.state == 3:
                toRemove.append(socket)
                continue
            if socket != websocket:
                await socket.send(message)

        # remove closed sockets
        for s in toRemove:
            sockets.remove(s)

async def main():
    async with serve(echo, "localhost", 10000) as server:
        await server.serve_forever()

asyncio.run(main())

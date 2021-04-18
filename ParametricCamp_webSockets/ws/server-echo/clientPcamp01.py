import websockets
import asyncio
import random

#url = "ws://simple-web-socket-server-echosecg.glitch.me/"
#url = "ws://127.0.0.1:5000"

async def listen():
    url = "ws://127.0.0.1:5000"
    async with websockets.connect(url) as websocket:
        msg = "Hello from Pcamp"
        print(f'Sending[{msg}] to connection [{id(websocket)}]')
        await websocket.send(msg)

        while True:
            got_back = await websocket.recv()
            print(f"Got: {got_back}")



loop = asyncio.get_event_loop()
loop.run_until_complete(listen())




#Reference https://github.com/adnantium/websocket_client_server/blob/master/websocket_client.py
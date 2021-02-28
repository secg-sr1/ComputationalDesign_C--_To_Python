import asyncio
import datetime
import random
import websockets

PORT = 5000

connected = set()

#Current date Server listening and PORT 
print(datetime.datetime.utcnow().isoformat() + " Server is listening on port " + str(PORT))



async def echo(websocket, path):
  #Register
  connected.add(websocket)
  #Some feedback on the console
  print("A client just connected")

  #Attach some behaviour to the incoming socket
  try:
    async for message in websocket:
      print("Received message from client: " + message)
      for conn in connected:
        await conn.send(f'Someone said: {message}')
    
  finally:
    #Unregister
    connected.remove(websocket)

start_server = websockets.serve(echo, "localhost", PORT)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

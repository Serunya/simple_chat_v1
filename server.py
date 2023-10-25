# https://www.youtube.com/watch?v=dgVCZtLqoV0&ab_channel=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9%D0%98%D0%B2%D0%B0%D0%BD%D0%BE%D0%B2%7CPython

import asyncio
import websockets
import sqlite3
import json

clients = []

async def check_clients():
    # await asyncio.sleep(3)
    print('______________________________', clients)

async def send_message(message):
    for client in clients:
        try:
            await client.send(message['name']+': '+message['message'])
        except Exception as e:
            print(e, '_________________________________________')
            clients.remove(client)

async def new_client_connetion(client_socket, path: str):
    print('New client connected: ', client_socket)
    if client_socket in clients:
        print('Такой клиент есть!')
        clients.remove(client_socket)
    else:
        clients.append(client_socket)
     
    while True:
        new_message = await client_socket.recv()
        new_message = json.loads(new_message)
        print('Client send a new message:', new_message)
        await check_clients()
        print(new_message)
        await send_message(message=new_message)
        

async def start_server():
    async with websockets.serve(new_client_connetion, 'localhost', 12345):
        await asyncio.Future()

if __name__ == '__main__':
    asyncio.run(start_server())
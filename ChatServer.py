import asyncio
from asyncio import StreamReader, StreamWriter

from ConnectionPool import ConnectionPool


class ChatServer:

    def __init__(self):
        self.connection_pool = ConnectionPool()

    async def handle_connection(self, reader: StreamReader, writer: StreamWriter):
        writer.write("Choose your Nickname: ".encode())

        response = await reader.readuntil(b"\n")
        writer.nickname = response.decode().strip()

        self.connection_pool.add_new_user_to_pool(writer)
        self.connection_pool.send_welcome_message(writer)

        await writer.drain()
        writer.close()
        await writer.wait_closed()

    async def main(self):
        server = await asyncio.start_server(self.handle_connection, host="0.0.0.0", port=8888)

        async with server:
            await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(ChatServer().main())

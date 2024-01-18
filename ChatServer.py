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
        self.connection_pool.broadcast_user_join(writer)

        # Цикл для поддержания соединения
        while True:
            try:
                data: bytes = await reader.readuntil(b"\n")
            except asyncio.exceptions.IncompleteReadError:
                self.connection_pool.broadcast_user_quit(writer)
                break

            message = data.decode().strip()
            match message:
                case "/quit":
                    self.connection_pool.broadcast_user_quit(writer)
                    break
                case "/list":
                    self.connection_pool.get_users_list(writer)
                case _:
                    self.connection_pool.broadcast_new_message(writer, message)

        await writer.drain()
        writer.close()
        await writer.wait_closed()
        self.connection_pool.remove_user_from_pool(writer)

    async def main(self):
        server = await asyncio.start_server(self.handle_connection, host="0.0.0.0", port=8888)

        async with server:
            await server.serve_forever()


if __name__ == '__main__':
    # для подключения клиентом "nc/telnet 127.0.0.1 8888
    asyncio.run(ChatServer().main())

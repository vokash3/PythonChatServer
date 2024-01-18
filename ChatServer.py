import asyncio
from asyncio import StreamReader, StreamWriter


class ChatServer:

    async def handle_connection(self, reader: StreamReader, writer: StreamWriter):
        writer.write("Hello! Type smt!".encode())

        data = await reader.readuntil(b"\n")

        writer.write("U sent: ".encode() + data)
        await writer.drain()

        writer.close()
        await writer.wait_closed()

    async def main(self):
        server = await asyncio.start_server(self.handle_connection, host="0.0.0.0", port=8888)

        async with server:
            await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(ChatServer().main())

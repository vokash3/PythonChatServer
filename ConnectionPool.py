from asyncio import StreamWriter, StreamReader


class ConnectionPool:
    def __init__(self):
        self.connection_pool = set()

    def send_welcome_message(self, writer: StreamWriter):
        pass

    def broadcast(self, writer: StreamWriter, message: str):
        pass

    def broadcast_user_join(self, writer: StreamWriter):
        pass

    def broadcast_user_quit(self, writer: StreamWriter):
        pass

    def broadcast_new_message(self, writer: StreamWriter, message: str):
        pass

    def get_users_list(self, writer: StreamWriter):
        pass

    def add_new_user_to_pool(self, writer: StreamWriter):
        pass

    def remove_user_from_pool(self, writer: StreamWriter):
        pass

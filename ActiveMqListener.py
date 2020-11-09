from stomp.listener import ConnectionListener

class ActiveMqListener(ConnectionListener):
    def __init__(self, host_ip, host_port) -> None:
        self.host_ip = host_ip
        self.host_port = host_port

    def on_connected(self, headers, body) -> None:
        print(f"Connected to {self.host_ip} on port {self.host_port}")

    def on_error(self, headers, body) -> None:
        print(f"received error: {body}")  

    def on_message(self, headers, body) -> None:
        print(f"Received message: {body}")

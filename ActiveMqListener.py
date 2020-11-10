from stomp.listener import ConnectionListener

class ActiveMqListener(ConnectionListener):
    def on_error(self, headers, body) -> None:
        print(f"received error: {body}")  

    def on_message(self, headers, body) -> None:
        queue = "destination"
        print(f"Received message: '{body}' from queue: {headers[queue]}")
        print(f"Headers:")

        for header_key in headers:
            print(f"{header_key} - {headers[header_key]} \n")

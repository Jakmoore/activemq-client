from stomp.listener import ConnectionListener

class ActiveMqListener(ConnectionListener):
    def on_error(self, frame):
        print(f"received an error: {frame.body}")  

    def on_message(self, headers, body):
        print("received")

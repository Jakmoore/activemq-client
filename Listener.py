class Listener(object):
    def on_error(self, headers, message):
        print(f"received an error {message}")  

    def on_message(self, headers, message):
        print("received a message")
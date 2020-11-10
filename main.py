import socket
import stomp
import time
from ActiveMqListener import ActiveMqListener

def main() -> None:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    host_port = 61613
    queue = "test_queue"
    conn = stomp.Connection([(host_ip, host_port)])

    if try_connection(conn, host_ip, host_port):
        subscribe(conn, queue, host_ip, host_port)
        send_message(conn, queue)
        time.sleep(1)
        conn.disconnect()

def try_connection(conn, host_ip, host_port) -> bool:
    try:
        print(f"Connecting to {host_ip} on port {host_port}")
        conn.connect("admin", "admin", wait=True)
        print("Successfully connected to message broker")
        return True
    except:
        return False

def subscribe(conn, queue, host_ip, host_port) -> None:
    conn.set_listener("", ActiveMqListener())
    conn.subscribe(queue, 1, "auto")

def send_message(conn, queue) -> None:
    print(f"Sending message to queue: {queue}")
    message = "TEST MESSAGE"
    conn.send(queue, message)
    
if __name__ == "__main__":
    main()
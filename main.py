import socket
import stomp
import time
from stomp.listener import PrintingListener
from ActiveMqListener import ActiveMqListener

def main() -> None:
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    host_port = 61613
    queue = "test_queue"
    conn = stomp.Connection([(host_ip, host_port)])
    connect_and_subscribe(conn, queue, host_ip, host_port)
    send_message(conn, queue)
    time.sleep(1)
    conn.disconnect()

def connect_and_subscribe(conn, queue, host_ip, host_port) -> None:
    conn.connect("admin", "admin", wait=True)
    conn.set_listener("", ActiveMqListener(host_ip, host_port))
    conn.subscribe(queue, 1, "auto")

def send_message(conn, queue) -> None:
    message = "TEST MESSAGE"
    conn.send(queue, message)
    
if __name__ == "__main__":
    main()
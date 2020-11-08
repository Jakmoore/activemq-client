import socket
import stomp
from stomp.listener import PrintingListener
from ActiveMqListener import ActiveMqListener

def main():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    queue = "test_queue"
    conn = stomp.Connection([(host_ip, 61613)])
    connect_and_subscribe(conn, queue)
    send_message(conn, queue)
    conn.disconnect()

def connect_and_subscribe(conn, queue):
    conn.connect("admin", "admin", wait=True)
    conn.set_listener("", PrintingListener())
    conn.subscribe(queue, 1, "auto")

def send_message(conn, queue):
    message = "TEST MESSAGE"
    conn.send(queue, message)
    
if __name__ == "__main__":
    main()
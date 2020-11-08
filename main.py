from Listener import Listener
import socket
import stomp

def main():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    queue = "test_queue"
    conn = stomp.Connection([(host_ip, 61613)])
    conn.set_listener("", Listener())
    conn.connect("admin", "admin", wait=True)
    conn.subscribe(queue, 1)
    send_message(conn, queue)

def send_message(conn, queue):
    message = "TEST MESSAGE"
    conn.send(queue, message)
    
if __name__ == "__main__":
    main()
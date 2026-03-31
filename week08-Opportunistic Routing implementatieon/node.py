import socket
import threading
import time
from config import HOST, BASE_PORT, PEER_PORTS, BUFFER_SIZE, FORWARD_THRESHOLD, UPDATE_INTERVAL
from delivery_table import DeliveryTable

delivery_table = DeliveryTable()
message_queue = []

def send_message(peer_port, message):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((HOST, peer_port))
        s.sendall(message.encode())
        s.close()
        print(f"[NODE {BASE_PORT}] Sent: {message} to {peer_port}")
        return True
    except (ConnectionRefusedError, socket.timeout):
        return False

def forward_loop():
    while True:
        candidates = delivery_table.get_best_candidates(FORWARD_THRESHOLD)
        for msg in message_queue[:]:
            for peer in candidates:
                if send_message(peer, msg):
                    message_queue.remove(msg)
                    break  # Stop after successful forward
        time.sleep(UPDATE_INTERVAL)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, BASE_PORT))
    server.listen()
    print(f"[NODE {BASE_PORT}] Listening for incoming messages...")
    while True:
        conn, addr = server.accept()
        data = conn.recv(BUFFER_SIZE).decode()
        print(f"[NODE {BASE_PORT}] Received: {data} from {addr}")
        message_queue.append(data)
        conn.close()

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    threading.Thread(target=forward_loop, daemon=True).start()

    # Example: Initialize delivery probabilities
    for peer in PEER_PORTS:
        delivery_table.update_probability(peer, 0.6)  # Assume precomputed probabilities

    # Example: Send initial messages opportunistically
    for peer in PEER_PORTS:
        msg = f"Hello from node {BASE_PORT}"
        if not send_message(peer, msg):
            print(f"[NODE {BASE_PORT}] Could not deliver to {peer}, storing in queue")
            message_queue.append(msg)

    while True:
        time.sleep(1)
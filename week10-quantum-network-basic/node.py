import socket
import threading
import time
from config import HOST, BASE_PORT, PEER_PORTS, BUFFER_SIZE, UPDATE_INTERVAL
from token import Token

token_queue = []

def send_token(peer_port, token):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((HOST, peer_port))
        s.sendall(token.message.encode())
        s.close()
        print(f"[NODE {BASE_PORT}] 🚀 Sent token to {peer_port}")
        return True
    except (ConnectionRefusedError, socket.timeout):
        # แอบปิด print แจ้งเตือนเวลาส่งไม่ผ่านไว้ จะได้ไม่รกหน้าจอเกินไปครับ
        return False

def forward_loop():
    while True:
        for token in token_queue[:]:
            for peer in PEER_PORTS:
                if send_token(peer, token):
                    token_queue.remove(token)
                    break
        time.sleep(UPDATE_INTERVAL)

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, BASE_PORT))
    server.listen()
    print(f"[NODE {BASE_PORT}] 📡 Listening for incoming tokens...")
    while True:
        conn, addr = server.accept()
        data = conn.recv(BUFFER_SIZE).decode()
        token = Token(data)
        
        # ลองเปิดอ่านครั้งแรก
        message = token.read_token()
        if message:
            print(f"[NODE {BASE_PORT}] 🔓 Received token: {message}")
            
            # --- ไฮไลต์ของ Lab นี้: พิสูจน์ว่าอ่านซ้ำไม่ได้! ---
            collapsed = token.read_token()
            print(f"[NODE {BASE_PORT}] 💥 Attempting to read again... Result: {collapsed} (State Collapsed!)")
            # -----------------------------------------------
            
            token_queue.append(token)
        else:
            print(f"[NODE {BASE_PORT}] ❌ Token invalid or already read from {addr}")
        conn.close()

if __name__ == "__main__":
    threading.Thread(target=start_server, daemon=True).start()
    threading.Thread(target=forward_loop, daemon=True).start()

    # Send initial token
    initial_token = Token(f"Quantum token from {BASE_PORT}")
    token_queue.append(initial_token)

    while True:
        time.sleep(1)
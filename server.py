import socket
import cv2
import pickle
import struct

PORT = 5050

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(("", PORT))

server_socket.listen(5)
print(f"Server Ip address: {socket.gethostbyname(socket.gethostname())}")

client_socket, client_address = server_socket.accept()
print(f"{client_address[0]}:{client_address[1]} Connected!")

data = b""
payload_size = struct.calcsize("Q")

print("Press 'q' to quit")

while True:
    while len(data) < payload_size:
        packet = client_socket.recv(32768)
        if not packet:
            break

        data += packet

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("Q", packed_msg_size)[0]

    while len(data) < msg_size:
        data += client_socket.recv(32768)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    frame = pickle.loads(frame_data)

    cv2.imshow("frame", frame)
    if cv2.waitKey(1) == ord("q"):
        break

client_socket.close()
server_socket.close()
cv2.destroyAllWindows()

import socket
import cv2
import pickle
import struct

PORT = 5050

cam = cv2.VideoCapture(0)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("SERVER IP ADDRESS", PORT))

while True:
    ret, frame = cam.read()
    if not ret:
        break

    data = pickle.dumps(frame)
    message_size = struct.pack("Q", len(data))

    try:
        client_socket.sendall(message_size + data)
    except ConnectionResetError:
        print("Connection error")
        break

cam.release()
client_socket.close()
cv2.destroyAllWindows()

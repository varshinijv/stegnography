import cv2

img = cv2.imread("encryptedImage.png")
if img is None:
    print("Error: Image not found!")
    exit()

c = {i: chr(i) for i in range(255)}

msg_length = img[0, 0, 0]

m, n, z = 1, 0, 0
full_msg = ""

for _ in range(msg_length):
    full_msg += c[img[n, m, z]]
    n += 1
    m += 1
    z = (z + 1) % 3

try:
    stored_password, message = full_msg.split("|", 1)
except ValueError:
    print("Error: Decryption failed! Incorrect message format.")
    exit()

password = input("Enter passcode for Decryption: ")

if password == stored_password:
    print("Decryption message:", message)
else:
    print("Incorrect password! Access denied.")

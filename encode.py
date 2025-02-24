import cv2
import os

img = cv2.imread("city.jpg")
if img is None:
    print("Error: Image not found!")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

d = {chr(i): i for i in range(255)}

msg = password + "|" + msg
msg_length = len(msg)


img[0, 0, 0] = msg_length

m, n, z = 1, 0, 0
for char in msg:
    img[n, m, z] = d[char]
    n += 1
    m += 1
    z = (z + 1) % 3

cv2.imwrite("encryptedImage.png", img)
os.system("start encryptedImage.png")

print("Message encoded successfully!")

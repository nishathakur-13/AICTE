import cv2
import os

# Load the image
img = cv2.imread("adi.jpeg")  # Ensure correct path
if img is None:
    print("Error: Image not found or cannot be read.")
    exit()

msg = input("Enter secret message: ")
password = input("Enter a passcode: ")

# Dictionary for encoding/decoding
d = {chr(i): i for i in range(256)}
c = {i: chr(i) for i in range(256)}

# Get image dimensions
height, width, _ = img.shape

# Encoding message in image
for i in range(len(msg)):
    n, m = divmod(i, width)  # Ensure indices stay within image bounds
    img[n, m, 0] = d[msg[i]]  # Modify only the first channel (R/G/B)

# Save encrypted image
cv2.imwrite("encryptedImage.jpg", img)

# Open the image (Mac & Windows support)
if os.name == "nt":  # Windows
    os.system("start encryptedImage.jpg")
else:  # macOS/Linux
    os.system("open encryptedImage.jpg")

# Decryption process
message = ""
pas = input("Enter passcode for decryption: ")

if password == pas:
    for i in range(len(msg)):
        n, m = divmod(i, width)
        message += c[img[n, m, 0]]
    print("Decryption message:", message)
else:
    print("YOU ARE NOT AUTHORIZED!")

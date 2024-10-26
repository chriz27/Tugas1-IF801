import numpy as np
import imageio  as img
import matplotlib.pyplot as plt

image = img.imread("borobudur.jpeg")

red = image[:,:,0]
green = image[:,:,1]
blue = image[:,:,2]

plt.figure(figsize=(15,5))
plt.subplot(1,4,1)
plt.title("Gambar Asli (Original Image)", fontsize=12)
plt.imshow(image)

# ---- RED CHANNEL ----
imgRed = np.zeros_like(image)
imgRed[:,:,0] = red
plt.subplot(1,4,2)
plt.title("Saluran Merah (Red Channel)", fontsize=12)
plt.imshow(imgRed)

# ---- GREEN CHANNEL ----
imgGreen = np.zeros_like(image)
imgGreen[:,:,1] = green
plt.subplot(1,4,3)
plt.title("Saluran Hijau (Green Channel)", fontsize=12)
plt.imshow(imgGreen)

# ---- BLUE CHANNEL ----
imgBlue = np.zeros_like(image)
imgBlue[:,:,2] = blue
plt.subplot(1,4,4)
plt.title("Saluran Biru (Blue Channel)", fontsize=12)
plt.imshow(imgBlue)

#plt.tight_layout()
plt.show()
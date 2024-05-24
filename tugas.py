import cv2
import matplotlib.pyplot as plt

# Membaca gambar
image = cv2.imread('dora.jpg')

# Menampilkan gambar asli
plt.figure(figsize=(10, 10))
plt.subplot(2, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Sebelum Berubah')
plt.axis('off')

# Konversi ke grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
plt.subplot(2, 2, 2)
plt.imshow(gray_image, cmap='gray')
plt.title('Setelah Diubah Menjadi Grayscale')
plt.axis('off')

# Deteksi tepi dengan Canny
edges = cv2.Canny(gray_image, 100, 200)
plt.subplot(2, 2, 3)
plt.imshow(edges, cmap='gray')
plt.title('Setelah Diubah Menjadi Edge Detection (Canny)')
plt.axis('off')

# Pengaburan dengan Gaussian Blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)
plt.subplot(2, 2, 4)
plt.imshow(cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB))
plt.title('Setelah Diubah Menjadi Blurred (Gaussian Blur)')
plt.axis('off')

plt.show()

import cv2
import matplotlib.pyplot as plt
import numpy as np

# Dizin yolu doğru bir şekilde belirtilmelidir
path = "../images/low_contrast.jpg"

# Resim dosyasını oku
img = cv2.imread(path, 0)

# cv2.calcHist(image, channel, No mask, 256 bins, possible range of histogram)
hist = cv2.calcHist([img], [0], None, [256], [0, 256])

# Histogramı çiz
plt.plot(hist)
plt.title('Grayscale Histogram')
plt.xlabel('Pixel Değeri')
plt.ylabel('Pixel Sayısı')
plt.show()


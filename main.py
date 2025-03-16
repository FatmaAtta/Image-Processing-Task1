import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Jellyfish.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #if you dont convert, the image will look different
plt.imshow(img)
plt.show()
#display channels
plt.subplot(1,3,1)
plt.imshow(img[:,:,0], cmap='Reds')
plt.subplot(1,3,2)
plt.imshow(img[:,:,1], cmap='Greens')
plt.subplot(1,3,3)
plt.imshow(img[:,:,2], cmap='Blues')
plt.show()
#another way to display the different channels by zeroing the other channels
red = img.copy()
red[:,:,1]=0
red[:,:,2]=0
plt.subplot(1,3,1)
plt.imshow(red)
green = img.copy()
green[:,:,0]=0
green[:,:,2]=0
plt.subplot(1,3,2)
plt.imshow(green)
blue = img.copy()
blue[:,:,0]=0
blue[:,:,1]=0
plt.subplot(1,3,3)
plt.imshow(blue)
plt.show()
#convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
plt.imshow(gray, cmap='gray')
plt.show()
#experimenting with histograms
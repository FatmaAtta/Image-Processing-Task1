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
plt.subplot(2,2,1)
freq, intervals, bars = plt.hist(gray.flatten(), 255, color='gray')
plt.title('Grayscale Histogram')
plt.subplot(2,2,2)
freq, intervals, bars = plt.hist(red.flatten(), 255, color='red')
plt.title('Red Histogram')
plt.subplot(2,2,3)
freq, intervals, bars = plt.hist(green.flatten(), 255, color='green')
plt.title('Green Histogram')
plt.subplot(2,2,4)
freq,intervals, bars = plt.hist(blue.flatten(), 255, color='blue')
plt.title('Blue Histogram')
plt.tight_layout()
plt.show()
#histogram equalization
eqGray = cv2.equalizeHist(gray)
plt.imshow(eqGray, cmap='gray')
plt.show()
plt.hist(eqGray.flatten(), 255, color='gray')
plt.show()

red, green, blue = cv2.split(img)
eqRed = cv2.equalizeHist(red)
eqGreen = cv2.equalizeHist(green)
eqBlue = cv2.equalizeHist(blue)

plt.subplot(1,3,1)
plt.imshow(eqRed, cmap='Reds')
plt.subplot(1,3,2)
plt.imshow(eqGreen, cmap='Greens')
plt.subplot(1,3,3)
plt.imshow(eqBlue, cmap='Blues')
plt.show()
eqImg = cv2.merge([eqRed, eqGreen, eqBlue])
plt.imshow(eqImg)
plt.show()




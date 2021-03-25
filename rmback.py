




from PIL import Image, ImageDraw
import cv2
import numpy as np
  

img = Image.open(r"img.jpeg").convert('RGBA')
  

seed = (0, 0)
  
rep_value = (0, 0, 0, 0)

ImageDraw.floodfill(img, seed, rep_value, thresh = 100)
  
img.show()
img.save("image2ch.png")


img = cv2.imread("image2ch.png")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)

color = cv2.bilateralFilter(img, 9, 300, 300)

cartoon = cv2.bitwise_and(color, color, mask=edges)

cv2.imshow("Cartoon", cartoon)

cv2.waitKey(0)
cv2.destroyAllWindows()
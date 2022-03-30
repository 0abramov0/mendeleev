import cv2 as cv
import numpy

hsv_min = numpy.array((0, 20, 25), numpy.uint8)
hsv_max = numpy.array((240, 255, 255), numpy.uint8)

img = cv.imread('apple.jpg')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
th = cv.inRange(hsv, hsv_min, hsv_max)

contours, hiarchy = cv.findContours(th.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
a = cv.drawContours(img, contours, -1, (255, 0, 0), 5, cv.LINE_AA, hiarchy, 1)

cv.imshow('th', a)
cv.waitKey()
cv.destroyAllWindows()

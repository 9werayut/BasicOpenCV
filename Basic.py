import cv2
img = cv2.imread("elephant.jpg", cv2.IMREAD_COLOR)
cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
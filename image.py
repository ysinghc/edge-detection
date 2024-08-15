import cv2

image = cv2.imread('input.jpg', cv2.IMREAD_GRAYSCALE)
blurred = cv2.GaussianBlur(image, (5, 5), 0)
edges = cv2.Canny(blurred, 100, 200)  # Lower and upper thresholds
cv2.imwrite('output.jpg', edges)

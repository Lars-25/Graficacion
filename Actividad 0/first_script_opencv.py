import cv2 as cv

# Load an image from file
image = cv.imread('Actividad 0/image.png',0)
# Display the image in a window
cv.imshow('First Image', image)
# Wait for a key press and close the window
cv.waitKey()
cv.destroyAllWindows

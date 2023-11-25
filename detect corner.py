#detect chessboard corners

import cv2
import numpy as np

# Load the image
image = cv2.imread('chess.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find the chessboard corners
ret, corners = cv2.findChessboardCorners(gray, (9, 11), None)

# If corners are found, refine the corner locations
if ret == True:
    cv2.cornerSubPix(gray, corners, (1, 1), (-1, -1), None)

    # Draw and display the corners
    cv2.drawChessboardCorners(image, (9, 11), corners, ret)

    # Show the image with corners
    cv2.imshow('Chessboard Corners', image)
    cv2.waitKey(0)

# Cleanup
cv2.destroyAllWindows()
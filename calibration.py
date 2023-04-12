import numpy as np
import cv2

# Define the dimensions of the checkerboard pattern
CHECKERBOARD_SIZE = (6, 8)

# Define the criteria to terminate the iterative process of finding the corners
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points (0,0,0), (1,0,0), ..., (5,7,0)
object_points = np.zeros((CHECKERBOARD_SIZE[0] * CHECKERBOARD_SIZE[1], 3), np.float32)
object_points[:, :2] = np.mgrid[0:CHECKERBOARD_SIZE[0], 0:CHECKERBOARD_SIZE[1]].T.reshape(-1, 2)

# Create empty lists to store object points and image points from all images
object_points_list = []  # 3d points in real world space
image_points_list = []  # 2d points in image plane


    # Load the calibration image
filename = f'C:/Users/PRATHAM/Downloads/Checkerboard-A4-30mm-8x6_page-0001.jpg'
img = cv2.imread(filename)

    # Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Find the corners of the checkerboard pattern
ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD_SIZE, None)

    # If corners are found, add object points and image points to the lists
if ret:
    object_points_list.append(object_points)
    corners = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    image_points_list.append(corners)

        # Draw the corners on the calibration image and display it
    cv2.drawChessboardCorners(img, CHECKERBOARD_SIZE, corners, ret)
    cv2.imshow('img', img)
    cv2.waitKey(500)

cv2.destroyAllWindows()

# Calibrate the camera using the object points and image points
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(object_points_list, image_points_list, gray.shape[::-1], None, None)

# Print the camera calibration parameters
print(f'Camera matrix:\n{mtx}\n')
print(f'Distortion coefficients:\n{dist}\n')

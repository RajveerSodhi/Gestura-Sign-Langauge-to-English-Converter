import numpy as np
import cv2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)

# Load the Image
image_path = "/Users/rajveersodhi/Desktop/archive/asl_alphabet_train/asl_alphabet_train/S/S1547.jpg"
imgo = cv2.imread(image_path)

if imgo is None:
    print(f"Error: Unable to load the image from the path: {image_path}")
else:
    height, width = imgo.shape[:2]

    # Create a mask holder
    mask = np.zeros(imgo.shape[:2], np.uint8)

    # Grab Cut the object
    bgdModel = np.zeros((1, 65), np.float64)
    fgdModel = np.zeros((1, 65), np.float64)

    # Hard Coding the Rect The object must lie within this rect.
    rect = (10, 10, width - 30, height - 30)
    cv2.grabCut(imgo, mask, rect, bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
    mask = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
    img1 = imgo * mask[:, :, np.newaxis]

    # Get the background
    background = imgo - img1

    # Change all pixels in the background that are not black to white
    background[np.where((background > [0, 0, 0]).all(axis=2))] = [0, 0, 0]

    # Add the background and the image
    final = background + img1

    # To be done - Smoothening the edges

    cv2.imshow('image', final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# import cv2
# import numpy as np
#
# def remove_background(image_path):
#     img = cv2.imread(image_path)
#     if img is None:
#         print(f"Error: Unable to load the image from the path: {image_path}")
#         return
#
#     mask = np.zeros(img.shape[:2], np.uint8)
#     bgd_model = np.zeros((1, 65), np.float64)
#     fgd_model = np.zeros((1, 65), np.float64)
#
#     rect = (10, 10, img.shape[1] - 30, img.shape[0] - 30)
#     cv2.grabCut(img, mask, rect, bgd_model, fgd_model, 5, cv2.GC_INIT_WITH_RECT)
#
#     mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
#     img_cut = img * mask2[:, :, np.newaxis]
#
#     # Display the original and processed images
#     cv2.imshow('Original Image', img)
#     cv2.imshow('Image with Background Removed', img_cut)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()
#
# # Input the image path here
# image_path = "/Users/rajveersodhi/Desktop/archive/asl_alphabet_train/asl_alphabet_train/S/S1547.jpg"
#
# remove_background(image_path)
#

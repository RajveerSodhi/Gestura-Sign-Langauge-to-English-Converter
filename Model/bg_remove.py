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

    # Change all pixels in the background that are not black to black
    background[np.where((background > [0, 0, 0]).all(axis=2))] = [0, 0, 0]

    # Add the background and the image with alpha blending
    alpha = 0.7  # You can adjust the alpha value for blending
    final = cv2.addWeighted(img1, alpha, background, 1 - alpha, 0)

    # Save the image with a valid file extension (e.g., PNG)
    save_path = "/Users/rajveersodhi/Desktop/output_image.png"
    cv2.imwrite(save_path, final)

    cv2.imshow('image', final)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# This file is a blueprint of config.py and does not get imported
# Copy the content of this file to config.py and change as required

CHANGE_IMG_FORMAT = False
ORIGINAL_IMG_FORMAT = "jpg"
IMG_FORMAT = "webp"

# RESIZE_FIXED_SIDE fixes one side and let othe other side adjust proportionately
RESIZE_ENABLED = True
RESIZE_FIXED_SIDE = "width"     # "width" or "height"
RESIZE_FIXED_SIDE_PX = 1600     # fixed width or fixed height in pixels
RESIZE_FIXED_SIDE_MIN_PX = 1601

ROTATE_IMAGE = False
ROTATE_ANGLE = 90

CROP_ENABLED = False
LEFT = 0    # left starting point in pixel (0 indicates the left edge)
UPPER = 0   # upper starting point in pixel (0 indicates the top edge)
RIGHT = 100 # ending point at right (100 will indicate the final image width will be 100px)
LOWER = 100 # ending point at bottom (100 will indicate the final image height will be 100px)
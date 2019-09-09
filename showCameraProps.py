import cv2
import numpy as np 

# I got tired of looking up the props-list, made a dict for future enhancements...
def get_prop_text(prop_number):
    prop_dict = {
    0:'CV_CAP_PROP_POS_MSEC Current position of the video file in milliseconds.',
    1:'CV_CAP_PROP_POS_FRAMES 0-based index of the frame to be decoded/captured next.',
    2:'CV_CAP_PROP_POS_AVI_RATIO Relative position of the video file',
    3:'CV_CAP_PROP_FRAME_WIDTH Width of the frames in the video stream.',
    4:'CV_CAP_PROP_FRAME_HEIGHT Height of the frames in the video stream.',
    5:'CV_CAP_PROP_FPS Frame rate.',
    6:'CV_CAP_PROP_FOURCC 4-character code of codec.',
    7:'CV_CAP_PROP_FRAME_COUNT Number of frames in the video file.',
    8:'CV_CAP_PROP_FORMAT Format of the Mat objects returned by retrieve() .',
    9:'CV_CAP_PROP_MODE Backend-specific value indicating the current capture mode.',
    10:'CV_CAP_PROP_BRIGHTNESS Brightness of the image (only for cameras).',
    11:'CV_CAP_PROP_CONTRAST Contrast of the image (only for cameras).',
    12:'CV_CAP_PROP_SATURATION Saturation of the image (only for cameras).',
    13:'CV_CAP_PROP_HUE Hue of the image (only for cameras).',
    14:'CV_CAP_PROP_GAIN Gain of the image (only for cameras).',
    15:'CV_CAP_PROP_EXPOSURE Exposure (only for cameras).',
    16:'CV_CAP_PROP_CONVERT_RGB Boolean flags indicating whether images should be converted to RGB.',
    17:'CV_CAP_PROP_WHITE_BALANCE Currently unsupported',
    18:'CV_CAP_PROP_RECTIFICATION Rectification flag for stereo cameras (note: only supported by DC1394 v 2.x backend currently)}'}

    return (prop_dict[prop_number])

# Make it readable by putting text and value on separate lines
def print_props():
    for x in range (19):
        print(get_prop_text(x))
        print(cap.get(x))


# Use cv2 to connect to camera get props and realease camera
cap = cv2.VideoCapture(0)

print_props()

cap.release()


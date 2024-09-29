import cv2
import numpy as np
from utils import height, width, one_pixel_size, fps, fileMap

def b2v(binary_string, file_extension):

    binary_string_size = len(binary_string)
    ind = 0
    video_name = 'video/video.mp4';
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    video = cv2.VideoWriter(video_name, fourcc, fps, (width, height), isColor = False)

    dataImg = np.zeros((height, width), dtype=np.uint8);

    # 1st frame contains data for file
    binary_representation_size = format(binary_string_size, '064b')
    binary_representation_extension = format(fileMap[file_extension], '064b')
    binary_iterable = 0 
    for x in range(0, height - one_pixel_size + 1, one_pixel_size):
        for y in range(0, width - one_pixel_size + 1, one_pixel_size):

            if(binary_iterable < 64):
                pixel_value = int(binary_representation_size[binary_iterable]) * 255
            elif(binary_iterable < 128):
                pixel_value = int(binary_representation_extension[binary_iterable % 64]) * 255
            else:
                break;
            dataImg[x:x+one_pixel_size, y:y+one_pixel_size] = pixel_value
            binary_iterable += 1

        if(binary_iterable == 128):
            break;

    video.write(dataImg);


    while ind < binary_string_size:
        img = np.zeros((height, width), dtype=np.uint8)
        for x in range(0, height - one_pixel_size + 1, one_pixel_size):
            for y in range(0, width - one_pixel_size + 1, one_pixel_size):
                if ind == binary_string_size:
                    break
                pixel_value = int(binary_string[ind]) * 255
                img[x:x+one_pixel_size, y:y+one_pixel_size] = pixel_value
                ind += 1
            if ind == binary_string_size:
                break
        video.write(img)
    video.release()
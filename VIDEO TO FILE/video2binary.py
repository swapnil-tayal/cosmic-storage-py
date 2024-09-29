import cv2
from utils import one_pixel_size as pixel_size
from utils import fileArray;

def v2b(video_path):

    cap = cv2.VideoCapture(video_path)
    binary_representation = ""
    isFirstFrame = 1;
    size = 0;
    extension = "";
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        heigth = gray_frame.shape[0]
        width = gray_frame.shape[1] 

        binary_representation_size = "";
        binary_representation_extension = "";
        if(isFirstFrame == 1):
            for i in range(0, heigth, pixel_size):
                for j in range(0, width, pixel_size):
                    avg_value = gray_frame[i, j]
                    binary_value = '1' if avg_value > 127 else '0'
                    if(len(binary_representation_size) < 64):
                        binary_representation_size += binary_value
                    elif(len(binary_representation_extension) < 64):
                        binary_representation_extension += binary_value
                    else:
                        break;
                if(len(binary_representation_size) == 64 and len(binary_representation_extension) == 64):
                    break;
            size = int(binary_representation_size, 2)
            extension = fileArray[int(binary_representation_extension, 2)]
            isFirstFrame = 0;
        else:
            for i in range(0, heigth, pixel_size):
                for j in range(0, width, pixel_size):

                    avg_value = gray_frame[i, j]
                    binary_value = '1' if avg_value > 127 else '0'

                    if(len(binary_representation) < size):
                        binary_representation += binary_value
                    else:
                        cap.release();
                        return [binary_representation, extension]
    
    cap.release()
    return [binary_representation, extension]
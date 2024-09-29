import os

height = 720
width = 1280
one_pixel_size = 8
fps = 60

fileMap = {
    ".mp4": 0,
    ".mp3": 1,
    ".png": 2,
    ".jpeg": 3,
    ".pdf": 4
}
fileArray = [".mp4", ".mp3", ".png", ".jpeg", ".pdf"];

def recreate_directory(dir_path):
    if os.path.exists(dir_path):
        for root, dirs, files in os.walk(dir_path, topdown=False):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                os.rmdir(os.path.join(root, dir))
        os.rmdir(dir_path)
    os.makedirs(dir_path)
# debug helper 

# Save the grayscale frame
# frame_number = int(cap.get(cv2.CAP_PROP_POS_FRAMES))  # Get current frame number
# gray_frame_filename = os.path.join(output_folder, f'frame_{frame_number}.png')
# cv2.imwrite(gray_frame_filename, gray_frame)

# write logs
# with open("binary.txt", "w") as file:
#     file.write(str)
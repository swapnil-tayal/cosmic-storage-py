import os
import file2binary
import binary2video
import utils

def main():

    input_folder_path = 'inputFile'
    utils.recreate_directory("video")
  
    for entry in os.listdir(input_folder_path):

        entry_path = os.path.join(input_folder_path, entry)
        if os.path.isfile(entry_path):
            
            file_extension = os.path.splitext(entry_path)[1]
            # print("File to binary start...");
            binary_string = file2binary.f2b(entry_path)
            # with open("binary.txt", "w") as file:
            #     file.write(binary_string)
            # print(len(binary_string))
            # print("File to binary done, Binary to video start...");
            binary2video.b2v(binary_string, file_extension)
            # print("Video created successfully!")
            
if __name__ == '__main__':
    main()

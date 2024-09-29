import os
import re
import video2binary
import binary2file
from utils import recreate_directory

def main():
    
    input_folder_path = 'video'
    recreate_directory("output");
  
    for entry in os.listdir(input_folder_path):

        entry_path = os.path.join(input_folder_path, entry)
        str, extension = video2binary.v2b(entry_path);
        binary2file.b2f(str, "output/out" + extension);

if __name__ == '__main__':
    main()
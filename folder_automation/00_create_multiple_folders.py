# simple python script to create multiple folders taken from a text file new line saperated
import os
import sys
import argparse


def create_folder(folder_path):
    os.mkdir(folder_path)

def read_text_file(file_path):
    try:
        f = open(file_path, "r")
        data = f.read()
        f.close()
        return data
    except FileNotFoundError:
        print("File not found")
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create Multiple folders from text file")
    parser.add_argument("text_file", type=str)
    parser.add_argument("parent_folder", type=str)
    args = parser.parse_args()

    files = read_text_file(args.text_file)
    parent_dir = args.parent_folder
    if files == None:
        print("Please supply text file with folder names to create!")
        print("program is exiting!")
        os.sys.exit()

    for fd in files.split("\n"):
        create_folder(os.path.join(parent_dir, fd))

    print("folders have been created!")

    


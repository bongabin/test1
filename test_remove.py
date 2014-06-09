import shutil
from distutils import dir_util
import traceback

import os


def main():

    dest = 'copy_dest'
    list_dir = os.walk(dest)
    for dirpath, dirnames, filenames in list_dir:
        print dirpath, dirnames, filenames




if __name__ == '__main__':
    main()

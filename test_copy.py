import shutil
from distutils import dir_util
import traceback


def test_cp_file_shutil():
    print 'test_cp_file_shutil'
    print ''

    src = 'test'
    dest = 'copy_dest/'
    try:
        shutil.copy(src, dest)
    except Exception:
        print traceback.format_exc()

def test_cp_file2_shutil():
    print 'test_cp_file_shutil'
    print ''

    src = 'test'
    dest = 'copy_dest/'
    try:
        shutil.copy2(src, dest)
    except Exception:
        print traceback.format_exc()


def test_cp_dir_shutil():
    print 'test_cp_utildist'
    print ''

    src = 'copy_src'
    dest = 'copy_dest'
    ignore = shutil.ignore_patterns('.git')

    try:
        # The destination directory, named by dst, must not already exist;
        #
        shutil.copytree(src, dest, ignore=ignore)
    except Exception:
        print traceback.format_exc()


def test_cp_distutils():
    print 'test_cp_utildist'
    print ''

    src = 'copy_src'
    dest = 'copy_dest'
    try:
        dir_util.copy_tree(src, dest)
    except Exception:
        print traceback.format_exc()


def main():
    #test_cp_file_shutil()
    test_cp_file2_shutil()

    #test_cp_dir_shutil()

    #test_cp_distutils()


if __name__ == '__main__':
    main()


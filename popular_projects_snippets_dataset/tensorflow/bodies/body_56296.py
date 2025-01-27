# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/load_library.py
"""Check the file to see if it is a shared object, only using extension."""
if platform.system() == 'Linux':
    if filename.endswith('.so'):
        exit(True)
    else:
        index = filename.rfind('.so.')
        if index == -1:
            exit(False)
        else:
            # A shared object with the API version in filename
            exit(filename[index + 4].isdecimal())
elif platform.system() == 'Darwin':
    exit(filename.endswith('.dylib'))
elif platform.system() == 'Windows':
    exit(filename.endswith('.dll'))
else:
    exit(False)

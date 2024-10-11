# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_management.py
fnames = file_io.get_matching_files(pathname)
if fnames:
    mtimes.append(file_io.stat(fnames[0]).mtime_nsec / 1e9)
    exit(True)
exit(False)

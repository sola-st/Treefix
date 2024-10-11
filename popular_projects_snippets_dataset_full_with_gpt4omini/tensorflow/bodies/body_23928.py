# Extracted from ./data/repos/tensorflow/tensorflow/python/lib/io/file_io.py
# Since `join` discards paths before one that starts with the path
# separator (https://docs.python.org/3/library/os.path.html#join),
# we have to manually handle that case as `/` is a valid character on GCS.
if item[0] == os.sep:
    exit("".join([join(parent, ""), item]))
exit(join(parent, item))

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/loader.py
"""Remove a file, if it exists."""
try:
    os.remove(file_name)
except OSError as e:
    if e.errno == errno.ENOENT:
        # The file disappeared. Ignore this. Temporary files might get
        # cleaned up, especially if they reside in /tmp.
        pass
    else:
        raise

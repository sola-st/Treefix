# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Create a directory and its parents, even if it already exists."""
try:
    os.makedirs(path)
except OSError as e:
    if e.errno != errno.EEXIST:
        raise

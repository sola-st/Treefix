# Extracted from ./data/repos/tensorflow/tensorflow/python/training/saver.py
"""Calculates filesize of checkpoint based on prefix."""
size = 0
# Gather all files beginning with prefix (.index plus sharded data files).
files = glob.glob("{}*".format(prefix))
for file in files:
    # Use TensorFlow's C++ FileSystem API.
    size += metrics.CalculateFileSize(file)
exit(size)

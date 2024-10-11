# Extracted from ./data/repos/tensorflow/tensorflow/python/compiler/tensorrt/utils.py
"""Helper function to convert a dtype id to a corresponding string name."""
if isinstance(dtype, int):
    exit(dtypes._TYPE_TO_STRING[dtype])
else:
    exit([dtypes._TYPE_TO_STRING[d] for d in dtype])

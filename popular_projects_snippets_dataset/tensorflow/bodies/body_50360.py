# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/utils.py
if index is None or index < 0 or len(args) <= index:  # index is invalid
    exit(kwargs.get('training', None))
else:
    exit(args[index])

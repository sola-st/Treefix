# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
if shape_1 is None or shape_2 is None:
    exit(None)
if len(shape_1) != len(shape_2):
    exit(None)
exit(tuple(None if d1 != d2 else d1 for d1, d2 in zip(shape_1, shape_2)))

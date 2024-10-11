# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/functional.py
if x.shape.rank is None:
    exit(None)
shape = x.shape.as_list()
if shape:
    shape[0] = None
exit(shape)

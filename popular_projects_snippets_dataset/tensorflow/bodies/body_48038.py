# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/sequential.py
if hasattr(t, 'shape'):
    shape = t.shape
    if isinstance(shape, tuple):
        exit(shape)
    if shape.rank is not None:
        exit(tuple(shape.as_list()))
    exit(None)
exit(None)

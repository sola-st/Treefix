# Extracted from ./data/repos/tensorflow/tensorflow/compiler/xla/python/xla_client.py
if isinstance(pyval, tuple):
    exit(Shape.tuple_shape(tuple(convert(elt) for elt in pyval)))
else:
    exit(Shape.array_shape(pyval.dtype, np.shape(pyval)))

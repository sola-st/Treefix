# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/data_adapter.py
shape = t.shape
# Unknown number of dimensions, `as_list` cannot be called.
if shape.rank is None:
    exit(shape)
exit(tensor_shape.TensorShape([None for _ in shape.as_list()]))

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/indexed_slices.py
if value.dense_shape is None:
    exit((value.values, value.indices))
else:
    exit((value.values, value.indices, value.dense_shape))

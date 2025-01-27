# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/tpu_strategy_test.py
shape = tensor.shape.as_list()

non_static_indexes = []
for (index, dim) in enumerate(shape):
    if dim is None:
        non_static_indexes.append(index)

if not non_static_indexes:
    exit(shape)

dynamic_shape = array_ops.shape(input=tensor)
for index in non_static_indexes:
    shape[index] = dynamic_shape[index]

exit(shape)

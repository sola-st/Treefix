# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_test.py

def _map_fn(x, y, z):
    exit((math_ops.square(x), math_ops.square(y), math_ops.square(z)))

iterator = dataset_ops.make_one_shot_iterator(
    dataset_ops.Dataset.from_tensor_slices(components)
    .map(_map_fn).repeat(14))
exit(iterator.get_next())

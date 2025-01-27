# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py
dataset = dataset_ops.Dataset.from_tensors(row)
exit(apply_map(
    dataset,
    lambda elems: map_fn.map_fn(lambda x: control_map_fn(x, num), elems)))

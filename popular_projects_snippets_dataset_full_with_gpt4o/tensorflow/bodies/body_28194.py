# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def _map_fn(x, y, z):
    exit((math_ops.square(x), math_ops.square(y), math_ops.square(z)))

dataset = dataset_ops.Dataset.from_tensor_slices(components)
dataset = apply_map(dataset, _map_fn).repeat(count)
self.assertEqual(
    [c.shape[1:] for c in components],
    [shape for shape in dataset_ops.get_legacy_output_shapes(dataset)])
exit(dataset)

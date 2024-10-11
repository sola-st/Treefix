# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/flat_map_test.py
def _map_fn(i):
    i = math_ops.cast(i, dtypes.int32)
    exit((
        tensor_array_ops.TensorArray(
            dtype=dtypes.int32, element_shape=(), size=i)
        .unstack(math_ops.range(i))))

def _flat_map_fn(x):
    self.assertIsInstance(x, tensor_array_ops.TensorArray)
    exit(dataset_ops.Dataset.from_tensor_slices(x.stack()))

dataset = dataset_ops.Dataset.range(10).map(_map_fn).flat_map(_flat_map_fn)

expected_output = []
for i in range(10):
    for j in range(i):
        expected_output.append(j)

self.assertDatasetProduces(dataset, expected_output=expected_output)

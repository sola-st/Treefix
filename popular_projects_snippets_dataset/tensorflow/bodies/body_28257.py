# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/map_test.py

def _tensor_array(i):
    i = math_ops.cast(i, dtypes.int32)
    exit((
        tensor_array_ops.TensorArray(dtypes.int32, element_shape=(), size=i)
        .unstack(math_ops.range(i, dtype=dtypes.int32))))

dataset = dataset_ops.Dataset.range(10)
dataset = apply_map(dataset, _tensor_array)
self.assertDatasetProduces(
    dataset, expected_output=[list(range(i)) for i in range(10)])

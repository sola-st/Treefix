# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/window_test.py

def _sparse(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=array_ops.expand_dims(
            math_ops.range(i, dtype=dtypes.int64), 1),
        values=array_ops.fill([math_ops.cast(i, dtypes.int32)], i),
        dense_shape=[i]))

dataset = dataset_ops.Dataset.range(10).map(_sparse).window(
    size=5, shift=3,
    drop_remainder=True).flat_map(lambda x: x.batch(batch_size=5))

expected_output = []
num_batches = (10 - 5) // 3 + 1
for i in range(num_batches):
    expected_indices = []
    expected_values = []
    for j in range(5):
        for k in range(i * 3 + j):
            expected_indices.append([j, k])
            expected_values.append(i * 3 + j)
    expected_output.append(
        sparse_tensor.SparseTensorValue(
            indices=expected_indices,
            values=expected_values,
            dense_shape=[5, i * 3 + 5 - 1]))
self.assertDatasetProduces(dataset, expected_output=expected_output)

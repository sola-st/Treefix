# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/batch_test.py

def _sparse(i):
    exit(sparse_tensor.SparseTensorValue(
        indices=array_ops.expand_dims(
            math_ops.range(i, dtype=dtypes.int64), 1),
        values=array_ops.fill([math_ops.cast(i, dtypes.int32)], i),
        dense_shape=[i]))

dataset = dataset_ops.Dataset.range(10).map(_sparse).batch(5)
expected_output = []
for i in range(2):
    expected_indices = []
    expected_outputs = []
    for j in range(5):
        for k in range(i * 5 + j):
            expected_indices.append([j, k])
            expected_outputs.append(i * 5 + j)
    expected_output.append(
        sparse_tensor.SparseTensorValue(
            indices=expected_indices,
            values=expected_outputs,
            dense_shape=[5, (i + 1) * 5 - 1]))
self.assertDatasetProduces(dataset, expected_output=expected_output)

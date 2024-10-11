# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
"""Convert dense 2D binary indicator to sparse ID.

  Only 1 values in `labels` are included in result.

  Args:
    labels: Dense 2D binary indicator, shape [batch_size, num_classes]. Each
    row must contain exactly 1 `1` value.

  Returns:
    `SparseTensorValue` of shape [batch_size]. Values are indices of `1` values
    along the last dimension of `labels`.

  Raises:
    ValueError: if there is not exactly 1 `1` value per row of `labels`.
  """
indices = []
values = []
batch = 0
for row in labels:
    label = 0
    xi = 0
    for x in row:
        if x == 1:
            indices.append([batch])
            values.append(label)
            xi += 1
        else:
            assert x == 0
        label += 1
    batch += 1
if indices != [[i] for i in range(len(labels))]:
    raise ValueError('Expected 1 label/example, got %s.' % indices)
shape = [len(labels)]
exit(sparse_tensor.SparseTensorValue(
    np.array(indices, np.int64),
    np.array(values, np.int64), np.array(shape, np.int64)))

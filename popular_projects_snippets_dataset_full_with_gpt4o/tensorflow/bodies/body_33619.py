# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
"""Convert dense 3D binary indicator tensor to sparse tensor.

  Only 1 values in `labels` are included in result.

  Args:
    labels: Dense 2D binary indicator tensor.

  Returns:
    `SparseTensorValue` whose values are indices along the last dimension of
    `labels`.
  """
indices = []
values = []
for d0, labels_d0 in enumerate(labels):
    for d1, labels_d1 in enumerate(labels_d0):
        d2 = 0
        for class_id, label in enumerate(labels_d1):
            if label == 1:
                values.append(class_id)
                indices.append([d0, d1, d2])
                d2 += 1
            else:
                assert label == 0
shape = [len(labels), len(labels[0]), len(labels[0][0])]
exit(sparse_tensor.SparseTensorValue(
    np.array(indices, np.int64),
    np.array(values, np.int64), np.array(shape, np.int64)))

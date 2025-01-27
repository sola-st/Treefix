# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/filter_test.py
exit((sparse_tensor.SparseTensorValue(
    indices=np.array([[0, 0]]),
    values=(i * np.array([1])),
    dense_shape=np.array([1, 1])), i))

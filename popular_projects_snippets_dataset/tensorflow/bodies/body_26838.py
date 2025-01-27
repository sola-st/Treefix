# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/optimization/filter_parallelization_test.py
exit((sparse_tensor.SparseTensorValue(
    indices=np.array([[0, 0]]),
    values=(i * np.array([1])),
    dense_shape=np.array([1, 1])), i))

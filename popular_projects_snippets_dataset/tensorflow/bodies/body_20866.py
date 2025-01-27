# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
for (dtype, index_type,
     use_gpu) in itertools.product([np.float16, np.float32, np.float64],
                                   [np.int32, np.int64], [False, True]):
    x_val = [np.arange(10), np.arange(10, 20), np.arange(20, 30)]
    y_val = [np.arange(1, 11), np.arange(11, 21), np.arange(21, 31)]
    x = np.array(x_val).astype(dtype)
    y = np.array(y_val).astype(dtype)
    lr = np.array(2.0).astype(dtype)
    grad_val = [np.arange(10), np.arange(10)]
    grad = np.array(grad_val).astype(dtype)
    indices = np.array([0, 2]).astype(index_type)
    self._testTypesForSparseAdagrad(x, y, lr, grad, indices, use_gpu)
    # Empty sparse gradients.
    empty_grad = np.zeros([0, 10], dtype=dtype)
    empty_indices = np.zeros([0], dtype=index_type)
    self._testTypesForSparseAdagrad(x, y, lr, empty_grad, empty_indices,
                                    use_gpu)

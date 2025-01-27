# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
for (dtype, index_type,
     use_gpu) in itertools.product([np.float16, np.float32, np.float64],
                                   [np.int32, np.int64], [False, True]):
    x_val = [[0.0], [0.0], [0.0]]
    y_val = [[4.0], [5.0], [6.0]]
    z_val = [[0.0], [0.0], [0.0]]
    x = np.array(x_val).astype(dtype)
    y = np.array(y_val).astype(dtype)
    z = np.array(z_val).astype(dtype)
    lr = np.array(2.0).astype(dtype)
    grad_val = [[1.5], [2.5]]
    grad = np.array(grad_val).astype(dtype)
    indices = np.array([0, 2]).astype(index_type)
    self._testTypesForSparseFtrl(x, y, z, lr, grad, indices, use_gpu)
    # Empty sparse gradients.
    empty_grad = np.zeros([0, 1], dtype=dtype)
    empty_indices = np.zeros([0], dtype=index_type)
    self._testTypesForSparseFtrl(x, y, z, lr, empty_grad, empty_indices,
                                 use_gpu)

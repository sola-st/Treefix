# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
for (dtype,
     index_type) in itertools.product([np.float16, np.float32, np.float64],
                                      [np.int32, np.int64]):
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
    self._testTypesForSparseFtrlMultiplyLinearByLr(x, y, z, lr, grad, indices)

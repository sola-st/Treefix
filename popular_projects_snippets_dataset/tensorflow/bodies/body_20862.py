# Extracted from ./data/repos/tensorflow/tensorflow/python/training/training_ops_test.py
for dtype in [np.float16, np.float32, np.float64]:
    x = np.arange(100).astype(dtype)
    y = np.arange(1, 101).astype(dtype)
    z = np.arange(102, 202).astype(dtype)
    lr = np.array(2.0).astype(dtype)
    l1 = np.array(3.0).astype(dtype)
    l2 = np.array(4.0).astype(dtype)
    grad = np.arange(100).astype(dtype)
    self._testTypesForFtrlMultiplyLinearByLr(
        x, y, z, lr, grad, use_gpu=False, l1=l1, l2=l2)

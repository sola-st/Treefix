# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/gather_op_test.py
params = np.array([[b"asdf", b"zxcv"], [b"qwer", b"uiop"]])
self.assertAllEqual([b"qwer", b"uiop"], array_ops.gather(params, 1, axis=0))
self.assertAllEqual([b"asdf", b"qwer"], array_ops.gather(params, 0, axis=1))

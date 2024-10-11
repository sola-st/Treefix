# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/topk_op_test.py
inputs = np.zeros([0, 10], dtype=np.float32)
self._validateTopK(inputs, 3, np.zeros([0, 3], dtype=np.float32),
                   np.zeros([0, 3], dtype=np.int32))

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/math_ops/in_topk_op_test.py
predictions = np.empty([0, 5])
target = np.empty([0], np.int32)
self._validateInTopK(predictions, target, 2, [])

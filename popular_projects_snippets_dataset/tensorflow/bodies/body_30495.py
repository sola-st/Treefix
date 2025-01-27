# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
# Only on_value provided
indices = [0, 1, 2]
depth = 3
truth = np.asarray([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.int32)
self._testBothOneHot(indices=indices, depth=depth, on_value=1, truth=truth)

# Only off_value provided
indices = [0, 1, 2]
depth = 3
truth = np.asarray([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.float32)
self._testBothOneHot(
    indices=indices, depth=depth, off_value=0.0, truth=truth)

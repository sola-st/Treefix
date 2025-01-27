# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/one_hot_op_test.py
indices = [0, 1, 2]
depth = 3
truth = np.asarray(
    [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]], dtype=np.float32)
self._testBothOneHot(indices=indices, depth=depth, truth=truth)

indices = [0, 1, 2]
depth = 3
truth = np.asarray([[1, 0, 0], [0, 1, 0], [0, 0, 1]], dtype=np.int32)
self._testBothOneHot(
    indices=indices, depth=depth, dtype=np.int32, truth=truth)

indices = [0, 1, 2]
depth = 3
truth = np.asarray([[1, -1, -1], [-1, 1, -1], [-1, -1, 1]], dtype=np.int32)
self._testBothOneHot(
    indices=indices, depth=depth, on_value=1, off_value=-1, truth=truth)

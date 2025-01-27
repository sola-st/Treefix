# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/ragged/ragged_from_tensor_op_test.py
# The examples from RaggedTensor.from_tensor.__doc__.
dt = constant_op.constant([[5, 7, 0], [0, 3, 0], [6, 0, 0]])
self.assertAllEqual(
    RaggedTensor.from_tensor(dt), [[5, 7, 0], [0, 3, 0], [6, 0, 0]])

self.assertAllEqual(
    RaggedTensor.from_tensor(dt, lengths=[1, 0, 3]), [[5], [], [6, 0, 0]])

self.assertAllEqual(
    RaggedTensor.from_tensor(dt, padding=0), [[5, 7], [0, 3], [6]])

dt_3d = constant_op.constant([[[5, 0], [7, 0], [0, 0]],
                              [[0, 0], [3, 0], [0, 0]],
                              [[6, 0], [0, 0], [0, 0]]])
self.assertAllEqual(
    RaggedTensor.from_tensor(dt_3d, lengths=([2, 0, 3], [1, 1, 2, 0, 1])),
    [[[5], [7]], [], [[6, 0], [], [0]]])

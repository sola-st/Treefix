# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/array_ops_test.py
with context.eager_mode():
    t = constant_op.constant([[1, 2, 3], [4, 5, 6]])
    paddings = constant_op.constant([[
        1,
        1,
    ], [2, 2]])
    padded = array_ops.pad(t, paddings, "CONSTANT")
    self.assertAllEqual(padded.numpy(),
                        [[0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 2, 3, 0, 0],
                         [0, 0, 4, 5, 6, 0, 0], [0, 0, 0, 0, 0, 0, 0]])

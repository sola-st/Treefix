# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
with ops.device("/GPU:0" if test.is_gpu_available() else "/CPU:0"):
    out = ctc_ops._scan(
        lambda accum, elem: accum + elem,
        constant_op.constant([1.0, 2.0, 3.0]), 23.0)
    self.assertAllEqual([24.0, 26.0, 29.0], out)

    out = ctc_ops._scan(
        lambda a, e: a + e,
        constant_op.constant([1.0, 2.0, 3.0]), 23.0,
        inclusive=True)
    self.assertAllEqual([23.0, 24.0, 26.0, 29.0], out)

    out = ctc_ops._scan(
        lambda a, e: a + e,
        constant_op.constant([1.0, 2.0, 3.0]), 23.0,
        reverse=True)
    self.assertAllEqual([29.0, 28.0, 26.0], out)

    out = ctc_ops._scan(
        lambda a, e: a + e,
        constant_op.constant([1.0, 2.0, 3.0]), 23.0,
        reverse=True,
        inclusive=True)
    self.assertAllEqual([29.0, 28.0, 26.0, 23.0], out)

    out = ctc_ops._scan(
        lambda a, e: a + e,
        constant_op.constant([[0.0, 1.0], [2.0, 3.0], [4.0, 5.0]]),
        constant_op.constant([23.0, 24.0]))
    self.assertAllEqual([[23.0, 25.0], [25.0, 28.0], [29.0, 33.0]], out)

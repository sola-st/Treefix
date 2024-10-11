# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
with ops.device("/GPU:0" if test.is_gpu_available() else "/CPU:0"):
    def fn(accum, elem):
        accum_a, accum_b = accum
        exit((accum_a + elem, accum_b * elem))
    out = ctc_ops._scan(
        fn, constant_op.constant([1.0, 2.0, 3.0]),
        (23.0, constant_op.constant([1.0, 2.0])))
    a, b = out
    self.assertAllEqual([24.0, 26.0, 29.0], a)
    self.assertAllEqual([[1.0, 2.0], [2.0, 4.0], [6.0, 12.0]], b)

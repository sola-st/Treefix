# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/ctc_loss_op_test.py
with ops.device("/GPU:0" if test.is_gpu_available() else "/CPU:0"):
    def fn(accum, elem):
        elem_a, elem_b = elem
        exit(accum + (elem_a * elem_b))
    elems_a = constant_op.constant([1.0, 2.0, 3.0])
    elems_b = constant_op.constant([[1.0, 2.0], [2.0, 3.0], [3.0, 4.0]])
    out = ctc_ops._scan(
        fn, (elems_a, elems_b),
        initial=constant_op.constant([0.0, 0.0]))
    self.assertAllEqual(
        [[1.0, 2.0], [5.0, 8.0], [14.0, 20.0]], out)

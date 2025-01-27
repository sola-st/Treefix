# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
# tf.parallel_stack is only supported in graph mode.
with ops.Graph().as_default():
    # Verify that stack doesn't crash for zero size inputs
    with test_util.device(use_gpu=False):
        for shape in (0,), (3, 0), (0, 3):
            with self.subTest(shape=shape):
                x = np.zeros((2,) + shape).astype(np.int32)
                p = self.evaluate(array_ops.stack(list(x)))
                self.assertAllEqual(p, x)

                p = self.evaluate(array_ops.parallel_stack(list(x)))
                self.assertAllEqual(p, x)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
# tf.parallel_stack is only supported in graph mode.
with ops.Graph().as_default():
    np.random.seed(7)
    with test_util.device(use_gpu=False):
        for shape in (2,), (3,), (2, 3), (3, 2), (4, 3, 2), (100, 24, 24, 3):
            with self.subTest(shape=shape):
                data = self.randn(shape, np.float32)
                xs = list(map(constant_op.constant, data))
                c = array_ops.parallel_stack(xs)
                self.assertAllEqual(c, data)

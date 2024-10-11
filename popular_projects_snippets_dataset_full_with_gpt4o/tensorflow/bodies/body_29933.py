# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
np.random.seed(7)
with test_util.use_gpu():
    # Verify that shape induction works with shapes produced via const stack
    a = constant_op.constant([1, 2, 3, 4, 5, 6])
    b = array_ops.reshape(a, array_ops.stack([2, 3]))
    self.assertAllEqual(b.get_shape(), [2, 3])

    # Check on a variety of shapes and types
    for shape in (2,), (3,), (2, 3), (3, 2), (4, 3, 2), (8, 2, 10):
        for dtype in [np.bool_, np.float32, np.int16, np.int32, np.int64]:
            with self.subTest(shape=shape, dtype=dtype):
                data = self.randn(shape, dtype)
                # Stack back into a single tensorflow tensor directly using np array
                c = array_ops.stack(data)
                if not context.executing_eagerly():
                    # This is implemented via a Const:
                    self.assertEqual(c.op.type, "Const")
                self.assertAllEqual(c, data)

                # Python lists also work for 1-D case:
                if len(shape) == 1:
                    data_list = list(data)
                    cl = array_ops.stack(data_list)
                    if not context.executing_eagerly():
                        self.assertEqual(cl.op.type, "Const")
                    self.assertAllEqual(cl, data)

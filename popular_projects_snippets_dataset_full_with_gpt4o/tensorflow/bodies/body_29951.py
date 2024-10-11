# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
with self.session():
    result = ops.convert_to_tensor([[[0., 0.],
                                     constant_op.constant([1., 1.])],
                                    np.array(
                                        [[2., 2.], [3., 3.]],
                                        dtype=np.float32)])
    self.assertAllEqual([[[0., 0.], [1., 1.]], [[2., 2.], [3., 3.]]],
                        self.evaluate(result))

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/stack_op_test.py
self.assertAllEqual([1, 0, 2],
                    ops.convert_to_tensor([1, constant_op.constant(0), 2]))
self.assertAllEqual([[0, 0, 0], [0, 1, 0], [0, 0, 0]],
                    ops.convert_to_tensor([[0, 0, 0],
                                           [0,
                                            constant_op.constant(1), 0],
                                           [0, 0, 0]]))
self.assertAllEqual([[0, 0, 0], [0, 1, 0], [0, 0, 0]],
                    ops.convert_to_tensor([[0, 0, 0],
                                           constant_op.constant([0, 1, 0]),
                                           [0, 0, 0]]))
self.assertAllEqual([[0, 0, 0], [0, 1, 0], [0, 0, 0]],
                    ops.convert_to_tensor([
                        constant_op.constant([0, 0, 0]),
                        constant_op.constant([0, 1, 0]),
                        constant_op.constant([0, 0, 0])
                    ]))

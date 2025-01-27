# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/convert_test.py
self.assertAllEqual([3, 6],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            tensor_shape.TensorShape([3, 6]))))
self.assertAllEqual([3, 6],
                    self.evaluate(convert.partial_shape_to_tensor((3, 6))))
self.assertAllEqual([3, 6],
                    self.evaluate(convert.partial_shape_to_tensor([3, 6])))
self.assertAllEqual([3, 6],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            constant_op.constant([3, 6],
                                                 dtype=dtypes.int64))))

self.assertAllEqual([3, -1],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            tensor_shape.TensorShape([3, None]))))
self.assertAllEqual([3, -1],
                    self.evaluate(
                        convert.partial_shape_to_tensor((3, None))))
self.assertAllEqual([3, -1],
                    self.evaluate(
                        convert.partial_shape_to_tensor([3, None])))
self.assertAllEqual([3, -1],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            constant_op.constant([3, -1],
                                                 dtype=dtypes.int64))))

self.assertAllEqual([-1, -1],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            tensor_shape.TensorShape([None, None]))))
self.assertAllEqual([-1, -1],
                    self.evaluate(
                        convert.partial_shape_to_tensor((None, None))))
self.assertAllEqual([-1, -1],
                    self.evaluate(
                        convert.partial_shape_to_tensor([None, None])))
self.assertAllEqual([-1, -1],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            constant_op.constant([-1, -1],
                                                 dtype=dtypes.int64))))

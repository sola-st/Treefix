# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/convert_test.py
self.assertAllEqual([],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            tensor_shape.TensorShape([]))))
self.assertAllEqual([], self.evaluate(convert.partial_shape_to_tensor(())))
self.assertAllEqual([], self.evaluate(convert.partial_shape_to_tensor([])))
self.assertAllEqual([],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            constant_op.constant([], dtype=dtypes.int64))))

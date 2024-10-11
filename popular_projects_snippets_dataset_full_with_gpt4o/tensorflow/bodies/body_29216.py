# Extracted from ./data/repos/tensorflow/tensorflow/python/data/util/convert_test.py
self.assertAllEqual([1],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            tensor_shape.TensorShape([1]))))
self.assertAllEqual([1], self.evaluate(
    convert.partial_shape_to_tensor((1,))))
self.assertAllEqual([1], self.evaluate(
    convert.partial_shape_to_tensor([1])))
self.assertAllEqual([1],
                    self.evaluate(
                        convert.partial_shape_to_tensor(
                            constant_op.constant([1], dtype=dtypes.int64))))

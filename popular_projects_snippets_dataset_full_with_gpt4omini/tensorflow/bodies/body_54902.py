# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
with self.assertRaisesRegex(ValueError,
                            "not defined on an unknown TensorShape"):
    tensor_shape.unknown_shape().as_list()
self.assertAllEqual([None, None], tensor_shape.unknown_shape(2).as_list())
self.assertAllEqual([2, None, 4],
                    tensor_shape.TensorShape((2, None, 4)).as_list())

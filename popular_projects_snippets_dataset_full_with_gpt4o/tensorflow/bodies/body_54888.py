# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/tensor_shape_test.py
self.assertEqual([3, 4, 7],
                 tensor_shape.TensorShape([3, 4, 7]).merge_with(
                     tensor_shape.TensorShape(None)).as_list())

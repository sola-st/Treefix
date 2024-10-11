# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
x = array_ops.placeholder(dtypes.float32, 1, name="x")
x_tensor_info = utils.build_tensor_info(x)
self.assertEqual("x:0", x_tensor_info.name)
self.assertEqual(types_pb2.DT_FLOAT, x_tensor_info.dtype)
self.assertEqual(1, len(x_tensor_info.tensor_shape.dim))
self.assertEqual(1, x_tensor_info.tensor_shape.dim[0].size)

# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
x = array_ops.sparse_placeholder(dtypes.float32, [42, 69], name="x")
x_tensor_info = utils.build_tensor_info(x)
self.assertEqual(x.values.name,
                 x_tensor_info.coo_sparse.values_tensor_name)
self.assertEqual(x.indices.name,
                 x_tensor_info.coo_sparse.indices_tensor_name)
self.assertEqual(x.dense_shape.name,
                 x_tensor_info.coo_sparse.dense_shape_tensor_name)
self.assertEqual(types_pb2.DT_FLOAT, x_tensor_info.dtype)
self.assertEqual(2, len(x_tensor_info.tensor_shape.dim))
self.assertEqual(42, x_tensor_info.tensor_shape.dim[0].size)
self.assertEqual(69, x_tensor_info.tensor_shape.dim[1].size)

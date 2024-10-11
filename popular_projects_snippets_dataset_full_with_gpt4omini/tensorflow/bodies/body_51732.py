# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
@def_function.function
def my_init_fn(x, y):
    self.x_var = x
    self.y_var = y

x = constant_op.constant(1, name="x")
y = constant_op.constant(2, name="y")
init_op_info = utils.build_tensor_info_from_op(my_init_fn(x, y))
self.assertEqual("PartitionedCall", init_op_info.name)
self.assertEqual(types_pb2.DT_INVALID, init_op_info.dtype)
self.assertEqual(0, len(init_op_info.tensor_shape.dim))

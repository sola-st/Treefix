# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/utils_test.py
x = constant_op.constant(1, name="x")
y = constant_op.constant(2, name="y")
z = control_flow_ops.group([x, y], name="op_z")
z_op_info = utils.build_tensor_info_from_op(z)
self.assertEqual("op_z", z_op_info.name)
self.assertEqual(types_pb2.DT_INVALID, z_op_info.dtype)
self.assertEqual(0, len(z_op_info.tensor_shape.dim))

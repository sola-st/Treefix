# Extracted from ./data/repos/tensorflow/tensorflow/compiler/mlir/tfr/integration/node_expansion_test.py
x = constant_op.constant([[1.0, 2.0], [3.0, 4.0], [5.0, 6.0]])

# Note: we purposely make multiple calls to VarHandleOp to exercise the
# cached kernal lookup path that was exhibiting the VarHandleOp import
# issue.
unused_ = gen_resource_variable_ops.VarHandleOp(
    dtype=dtypes.float32, shape=[3, 2])
handle = gen_resource_variable_ops.VarHandleOp(
    dtype=dtypes.float32, shape=[3, 2])
gen_resource_variable_ops.AssignVariableOp(resource=handle, value=x)
self.assertAllEqual(
    x,
    gen_resource_variable_ops.ReadVariableOp(
        resource=handle, dtype=dtypes.float32))

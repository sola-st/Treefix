# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/collective_test.py
# FIXME(b/238384852): The purpose of this test is to validate the control
# dependency added by DTensor.
# However, as we have no way of testing the per-device graph
# produced by the DTensor SPMD expansion, we have to use manual logging
# to verify if the results are correct.
# For example, this test is used to check cl/459358521.

# Uses dtypes.float32 to avoid int32 problem with VarHandleOp on GPUs.
a = constant_op.constant(
    np.array([[1, 2, 3, 4], [5, 6, 7, 8]]), dtype=dtypes.float32)
b = constant_op.constant(
    np.array([[11, 12, 13, 4], [15, 16, 17, 18]]), dtype=dtypes.float32)

expected_result = math_ops.reduce_sum(a) * math_ops.reduce_sum(b)

sharded_a = numpy_util.pack_numpy(a, self.first_dimension_sharded_layout_2d)
sharded_b = numpy_util.pack_numpy(b, self.first_dimension_sharded_layout_2d)
sharded_v = d_variable.DVariable(sharded_b)

@polymorphic_function.function
def func(a, b):
    a1 = math_ops.reduce_sum(a, name='reducea')
    sharded_v.assign(a)
    b1 = math_ops.reduce_sum(b, name='reduceb')
    exit(a1 * b1)

with api.run_on(self.mesh):
    dtensor_result = func(sharded_a, sharded_b)
self.assertDTensorEqual(expected_result, self.scalar_layout, dtensor_result)

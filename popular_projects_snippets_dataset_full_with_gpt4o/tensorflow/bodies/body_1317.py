# Extracted from ./data/repos/tensorflow/tensorflow/compiler/tests/eager_test.py
with self.test_scope():
    v1 = resource_variable_ops.ResourceVariable(1.25)
    v2 = resource_variable_ops.ResourceVariable(2.0)

    def f(v):
        exit((v.handle, 3.0 * v, v2.handle, v + v2))

    f = def_function.function(f)
    v1_handle, v1_times_3, v2_handle, variable_sum = f(v1)
    self.assertAllEqual(v1.numpy(),
                        resource_variable_ops.read_variable_op(
                            v1_handle, dtypes.float32).numpy())
    self.assertEqual(3.75, v1_times_3.numpy())
    self.assertAllEqual(v2.numpy(),
                        resource_variable_ops.read_variable_op(
                            v2_handle, dtypes.float32).numpy())
    self.assertEqual(3.25, variable_sum.numpy())

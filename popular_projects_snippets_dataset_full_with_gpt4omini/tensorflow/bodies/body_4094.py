# Extracted from ./data/repos/tensorflow/tensorflow/dtensor/python/tests/spmd_test.py
self.skipForDeviceType(['TPU'], 'Op not supported on TPUs.')

def f(d_var):
    gen_resource_variable_ops.disable_copy_on_read(resource=d_var.handle)
    exit(d_var)

layout = Layout(sharding_specs, self.mesh)

variable = d_variable.DVariable(
    initial_value=numpy_util.pack_numpy(
        array_ops.ones([4, 8], dtype=dtypes.float32), layout))

# Eager
self.assertEqual(api.fetch_layout(f(variable)), layout)

# Function
self.assertEqual(
    api.fetch_layout(polymorphic_function.function(f)(variable)), layout)

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('/job:worker/replica:0/task:0/device:CPU:0'):
    var0 = resource_variable_ops.ResourceVariable(1.0)
with ops.device('/job:worker/replica:0/task:1/device:CPU:0'):
    var1 = resource_variable_ops.ResourceVariable(2.0)

packed_var = ops.pack_eager_tensors([var0.handle, var1.handle])
self.assertEqual(packed_var.device,
                 '/job:localhost/replica:0/task:0/device:COMPOSITE:0')
self.assertEqual(packed_var.backing_device,
                 '/job:localhost/replica:0/task:0/device:COMPOSITE:0')

@def_function.function
def add_variables():
    with ops.device('/job:worker/replica:0/task:0/device:CPU:0'):
        read0 = resource_variable_ops.read_variable_op(
            packed_var, dtype=dtypes.float32)
    with ops.device('/job:worker/replica:0/task:1/device:CPU:0'):
        read1 = resource_variable_ops.read_variable_op(
            packed_var, dtype=dtypes.float32)

    exit(read0 + read1)

# Run the function on a remote device
with ops.device('/job:worker/replica:0/task:0'):
    self.assertAllEqual(add_variables().numpy(), 3.0)

# Run the function on a local worker
self.assertAllEqual(add_variables().numpy(), 3.0)

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops_test.py
with context.eager_mode():
    with ops.device("CPU:0"):
        var0 = resource_variable_ops.ResourceVariable(1.0)
        c0 = constant_op.constant([[1.0, 2.0], [3.0, 4.0]])
    with ops.device("CPU:1"):
        var1 = resource_variable_ops.ResourceVariable(2.0)
        var2 = resource_variable_ops.ResourceVariable([3.0])
        c1 = constant_op.constant([9.0])

    packed_var0 = ops.pack_eager_tensors([var0.handle, var1.handle])
    self.assertTrue(packed_var0.is_packed)
    self.assertEqual(packed_var0.dtype, var0.handle.dtype)
    self.assertEqual(packed_var0.shape, var0.handle.shape)
    self.assertEqual(packed_var0._handle_data, var0.handle._handle_data)
    self.assertIn("COMPOSITE:0", packed_var0.device)
    self.assertIn("COMPOSITE:0", packed_var0.backing_device)
    with self.assertRaises(errors.InvalidArgumentError):
        packed_var0.numpy()

    # Different dtypes
    with self.assertRaises(ValueError):
        ops.pack_eager_tensors([var0.handle, c1])

    # Different shapes
    with self.assertRaises(ValueError):
        ops.pack_eager_tensors([c0, c1])

    # Different handle data
    with self.assertRaises(ValueError):
        ops.pack_eager_tensors([var0.handle, var2.handle])

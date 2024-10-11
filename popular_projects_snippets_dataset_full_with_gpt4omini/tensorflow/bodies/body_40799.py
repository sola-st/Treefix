# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
self.assertRegex(handle.backing_device, 'CPU')
tensor = gen_resource_variable_ops.read_variable_op(
    handle, dtypes.float32)
self.assertEqual(tensor.numpy(), expected_value)

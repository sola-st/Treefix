# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
# Temporarily replace the context
# pylint: disable=protected-access
old_context = context.context()
context._set_context(context.Context())
try:
    config.set_device_policy('silent')
    config.set_soft_device_placement(True)
    cpu_tensor = constant_op.constant(1.0)
    result = cpu_tensor + cpu_tensor
    self.assertEqual(result.device,
                     '/job:localhost/replica:0/task:0/device:GPU:0')
finally:
    context._set_context(old_context)

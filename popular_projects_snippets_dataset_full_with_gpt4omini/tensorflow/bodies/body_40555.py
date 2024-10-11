# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/ops_test.py
# Temporarily replace the context
# pylint: disable=protected-access
old_context = context.context()
context._set_context(context.Context())
try:
    config.set_device_policy('silent')
    cpu_tensor = constant_op.constant(1.0)
    gpu_tensor = cpu_tensor.gpu()
    self.assertAllEqual(cpu_tensor + gpu_tensor, 2.0)
finally:
    context._set_context(old_context)

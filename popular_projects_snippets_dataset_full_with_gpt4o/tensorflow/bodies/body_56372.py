# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
self.assertEqual(context.DEVICE_PLACEMENT_SILENT,
                 context.context().device_policy)

# If no op has been executed we should be able to set the device policy as
# well as any init-time configs.
config.set_intra_op_parallelism_threads(1)
config.set_device_policy('silent')
config.set_intra_op_parallelism_threads(2)

context.ensure_initialized()

def copy_tensor(dtype=dtypes.int32):
    with ops.device('CPU:0'):
        cpu_tensor = constant_op.constant(1, dtype=dtype)
    gpu_tensor = cpu_tensor.gpu()
    self.assertAllEqual(cpu_tensor + gpu_tensor, 2.0)

config.set_device_policy('silent')
self.assertEqual(config.get_device_policy(), 'silent')
self.assertEqual(context.DEVICE_PLACEMENT_SILENT,
                 context.context().device_policy)
copy_tensor()

config.set_device_policy('silent_for_int32')
self.assertEqual(config.get_device_policy(), 'silent_for_int32')
self.assertEqual(context.DEVICE_PLACEMENT_SILENT_FOR_INT32,
                 context.context().device_policy)
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'Tensors on conflicting devices'):
    copy_tensor(dtypes.float32)
copy_tensor()

config.set_device_policy('warn')
self.assertEqual(config.get_device_policy(), 'warn')
self.assertEqual(context.DEVICE_PLACEMENT_WARN,
                 context.context().device_policy)
copy_tensor()

config.set_device_policy('explicit')
self.assertEqual(config.get_device_policy(), 'explicit')
self.assertEqual(context.DEVICE_PLACEMENT_EXPLICIT,
                 context.context().device_policy)
with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'Tensors on conflicting devices'):
    copy_tensor()

config.set_device_policy(None)
self.assertEqual(config.get_device_policy(), 'silent')

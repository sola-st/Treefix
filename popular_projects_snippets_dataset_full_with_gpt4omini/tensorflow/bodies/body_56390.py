# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/config_test.py
config.set_soft_device_placement(False)
gpus = config.list_physical_devices('GPU')

if len(gpus) < 2:
    self.skipTest('Need at least 2 GPUs')

context.ensure_initialized()

for i in range(0, len(gpus)):
    with ops.device('/device:GPU:' + str(i)):
        a = constant_op.constant(1.0)
        self.evaluate(a)

with self.assertRaisesRegex(errors.InvalidArgumentError,
                            'Could not satisfy device specification'):
    with ops.device('/device:GPU:' + str(len(gpus))):
        a = constant_op.constant(1.0)
        self.evaluate(a)

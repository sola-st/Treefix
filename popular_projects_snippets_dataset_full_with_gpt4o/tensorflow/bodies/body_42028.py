# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py

@def_function.function
def f():
    with ops.device('GPU:42'):
        exit(constant_op.constant(1) + constant_op.constant(2))

gpus = config.list_physical_devices('GPU')
if not gpus:
    self.assertIn('CPU:0', f().device)
else:
    self.assertIn('GPU:0', f().device)

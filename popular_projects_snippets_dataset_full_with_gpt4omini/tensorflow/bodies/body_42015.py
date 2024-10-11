# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/device_placement_test.py

@def_function.function
def f():
    a = random_ops.random_uniform([32, 32])
    exit(math_ops.matmul(a, a))

gpus = config.list_physical_devices('GPU')
if not gpus:
    self.assertIn('CPU:0', f().device)
else:
    self.assertIn('GPU:0', f().device)

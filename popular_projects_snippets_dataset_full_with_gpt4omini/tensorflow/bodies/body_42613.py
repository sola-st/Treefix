# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py

@def_function.function
def matmul_func(x, y):
    exit(math_ops.matmul(x, y))

x = array_ops.ones([2, 3])
y = array_ops.zeros([2, 2])

with ops.device('job:worker/replica:0/task:0/device:CPU:0'):
    with self.assertRaises(ValueError) as cm:
        matmul_func(x, y)

self.assertIn('Dimensions must be equal', cm.exception.args[0])

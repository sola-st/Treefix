# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/remote_test.py
with ops.device('job:worker/replica:0/task:0/device:CPU:0'):
    x = array_ops.ones([2, 3])
    y = array_ops.zeros([2, 2])
    with self.assertRaises(errors.InvalidArgumentError) as cm:
        math_ops.matmul(x, y)

self.assertIn('Dimensions must be equal', cm.exception.message)

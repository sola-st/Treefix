# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with ops.device('cpu:1'):
    x = array_ops.identity(1.0)
with ops.device('cpu:0'):
    y = array_ops.identity(x)
self.assertEqual(x.device, '/job:localhost/replica:0/task:0/device:CPU:1')
self.assertEqual(y.device, '/job:localhost/replica:0/task:0/device:CPU:0')

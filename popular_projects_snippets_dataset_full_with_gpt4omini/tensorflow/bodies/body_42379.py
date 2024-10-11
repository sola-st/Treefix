# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
cpu = context.device('cpu:0')
gpu = context.device('gpu:0')
cpu.__enter__()
self.assertEndsWith(current_device(), 'CPU:0')
gpu.__enter__()
self.assertEndsWith(current_device(), 'GPU:0')
with self.assertRaisesRegex(
    RuntimeError, 'Exiting device scope without proper scope nesting'):
    cpu.__exit__()
    self.assertEndsWith(current_device(), 'GPU:0')
gpu.__exit__()
self.assertEndsWith(current_device(), 'CPU:0')
cpu.__exit__()

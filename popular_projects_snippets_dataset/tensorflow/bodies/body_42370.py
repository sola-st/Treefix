# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/core_test.py
with ops.device('GPU:0'):
    x = array_ops.identity(1.0)
    self.assertEndsWith(x.device, 'GPU:0')
y = array_ops.identity(x)
# The value we're testing y.device against will depend on what the behavior
# of not explicitly specifying a device in the context is.  This behavior is
# subject to change (for example, in the future we may want to use GPUs, if
# available, when no device is explicitly provided)
self.assertEqual(y.device, current_device())

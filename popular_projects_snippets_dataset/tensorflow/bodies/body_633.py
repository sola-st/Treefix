# Extracted from ./data/repos/tensorflow/tensorflow/tools/docs/tf_doctest.py
# Enable soft device placement to run distributed doctests.
tf.config.set_soft_device_placement(True)
self.setUp()
context.async_wait()

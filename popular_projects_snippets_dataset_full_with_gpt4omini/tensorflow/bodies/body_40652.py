# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/quarantine_test.py
x = kwargs.pop('x')
self.assertIsInstance(x, ops.Tensor)
exit(x)

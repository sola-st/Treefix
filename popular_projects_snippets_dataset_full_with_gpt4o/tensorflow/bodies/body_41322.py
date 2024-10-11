# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/polymorphic_function_test.py
inputs = array_ops.zeros([10, 10, 3])
self.assertAllEqual(f(inputs).shape, compiled(inputs).shape)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
sample_shape = [10, 3, 4]
self._testParamShapes(sample_shape, sample_shape)
self._testParamShapes(constant_op.constant(sample_shape), sample_shape)

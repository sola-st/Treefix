# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/distributions/normal_test.py
sample_shape = [10, 3, 4]
self._testParamStaticShapes(sample_shape, sample_shape)
self._testParamStaticShapes(
    tensor_shape.TensorShape(sample_shape), sample_shape)

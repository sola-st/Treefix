# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/array_ops/shape_ops_test.py
for use_gpu in [False, True]:
    with self.cached_session(use_gpu=use_gpu):
        input_1x1x3 = np.zeros([1, 1, 3])
        self._compareSqueezeAll(input_1x1x3)
        self._compareSqueezeAll(input_1x1x3, [0])
        self._compareSqueezeAll(input_1x1x3, [1])
        self.assertRaises(ValueError, array_ops.squeeze, input_1x1x3, [2])

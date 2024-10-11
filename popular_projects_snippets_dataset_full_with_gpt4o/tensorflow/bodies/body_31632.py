# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
self._testDepthwiseMaxPoolInvalidConfig(
    [1, 2, 2, 4], [1, 2, 2, 2], [1, 1, 1, 2],
    "exactly one of pooling across depth")
self._testDepthwiseMaxPoolInvalidConfig(
    [1, 2, 2, 4], [1, 1, 1, 2], [1, 1, 1, 1],
    "depth window to equal the depth stride")
self._testDepthwiseMaxPoolInvalidConfig([1, 2, 2, 4], [1, 1, 1, 3],
                                        [1, 1, 1, 3], "evenly divide")
if test.is_gpu_available():
    with self.session():
        t = variables.Variable(np.ones([1, 2, 2, 4]))
        self.evaluate(variables.global_variables_initializer())
        with self.assertRaisesOpError("for CPU devices"):
            nn_ops.max_pool(
                t, ksize=[1, 1, 1, 2], strides=[1, 1, 1, 2],
                padding="SAME").eval()

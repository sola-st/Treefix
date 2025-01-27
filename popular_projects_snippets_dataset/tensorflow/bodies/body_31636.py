# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
tensor_input = [
    1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0,
    0.0, 1.0, 0.0, 1.0
]

Config = collections.namedtuple(
    "Config", ["use_gpu", "include_batch_in_index", "argmax", "Targmax"])
configs = [
    Config(False, False, [0, 1, 3, 5, 0, 2, 6, 8], dtypes.int64),
    Config(False, True, [0, 1, 3, 5, 9, 11, 15, 17], dtypes.int64),
    Config(False, False, [0, 1, 3, 5, 0, 2, 6, 8], dtypes.int32),
    Config(False, True, [0, 1, 3, 5, 9, 11, 15, 17], dtypes.int32),
    Config(True, False, [0, 1, 3, 5, 0, 2, 6, 8], dtypes.int64),
    Config(True, True, [0, 1, 3, 5, 9, 11, 15, 17], dtypes.int64),
]

for config in configs:
    with GetDeviceScope(self, use_gpu=config.use_gpu):
        t = constant_op.constant(tensor_input, shape=[2, 3, 3, 1])
        out_op, argmax_op = nn_ops.max_pool_with_argmax(
            t,
            ksize=[1, 2, 2, 1],
            strides=[1, 1, 1, 1],
            Targmax=config.Targmax,
            padding="VALID",
            include_batch_in_index=config.include_batch_in_index)
        out, argmax = self.evaluate([out_op, argmax_op])
        self.assertShapeEqual(out, out_op)
        self.assertShapeEqual(argmax, argmax_op)
        self.assertAllClose(out.ravel(),
                            [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
        self.assertAllEqual(argmax.ravel(), config.argmax)

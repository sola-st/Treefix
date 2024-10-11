# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
tensor_input = [89, 73, -109]
Config = collections.namedtuple("Config", ["use_gpu", "padding"])
configs = [
    Config(False, "SAME"),
    Config(False, "VALID"),
    Config(True, "SAME"),
    Config(True, "VALID"),
]

for config in configs:
    with GetDeviceScope(self, use_gpu=config.use_gpu):
        t = constant_op.constant(tensor_input, shape=[1, 1, 1, 3])
        out_op, argmax_op = nn_ops.max_pool_with_argmax(
            t,
            ksize=[1, 1, 1, 3],
            strides=[1, 1, 1, 3],
            padding=config.padding,
        )
        out, argmax = self.evaluate([out_op, argmax_op])
        # TODO(b/259733542): Fix below asserts once bug is fixed.
        # self.assertShapeEqual(out, out_op)
        # self.assertShapeEqual(argmax, argmax_op)
        self.assertAllClose(out.ravel(), [89, 73, -109])
        self.assertAllClose(argmax.ravel(), [0, 1, 2])

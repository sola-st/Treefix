# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
orig_input = [
    1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, 0.0, 1.0, 0.0, 0.0,
    0.0, 1.0, 0.0, 1.0
]
tensor_input = [11.0, 12.0, 13.0, 14.0, 21.0, 22.0, 23.0, 24.0]

Config = collections.namedtuple(
    "Config", ["use_gpu", "include_batch_in_index", "argmax"])
configs = [
    Config(False, False, [0, 1, 3, 5, 0, 2, 6, 8]),
    Config(False, True, [0, 1, 3, 5, 9, 11, 15, 17]),
    Config(True, False, [0, 1, 3, 5, 0, 2, 6, 8]),
    Config(True, True, [0, 1, 3, 5, 9, 11, 15, 17])
]

for config in configs:
    with GetDeviceScope(self, config.use_gpu):
        orig_in = constant_op.constant(orig_input, shape=[2, 3, 3, 1])
        t = constant_op.constant(tensor_input, shape=[2, 2, 2, 1])
        argmax_t = constant_op.constant(
            config.argmax, shape=[2, 2, 2, 1], dtype=dtypes.int64)
        out_op = gen_nn_ops.max_pool_grad_with_argmax(
            orig_in,
            t,
            argmax_t,
            ksize=[1, 2, 2, 1],
            strides=[1, 1, 1, 1],
            padding="VALID",
            include_batch_in_index=config.include_batch_in_index)
        out = self.evaluate(out_op).flatten()
        self.assertAllClose(out, [
            11.0, 12.0, 0.0, 13.0, 0.0, 14.0, 0.0, 0.0, 0.0, 21.0, 0.0, 22.0,
            0.0, 0.0, 0.0, 23.0, 0.0, 24.0
        ])

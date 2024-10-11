# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
with self.session(use_gpu=test.is_gpu_available()) as sess:
    with self.assertRaisesRegexp(
        (errors_impl.UnimplementedError, errors_impl.InvalidArgumentError),
        "Right padding 2 needs to be smaller than the window size 2|"
        "XLA does not support pooling ops with explicit padding"):
        input_sizes = [1, 3, 3, 1]
        x = [(((f + 128) % 255) - 127) for f in range(9)]
        t = constant_op.constant(x, shape=input_sizes, dtype=dtypes.float32)
        sess.run(gen_nn_ops.max_pool(
            t,
            ksize=[1, 2, 2, 1],
            strides=[1, 2, 2, 1],
            padding="EXPLICIT",
            explicit_paddings=[0, 0, 0, 1, 0, 2, 0, 0],
            data_format="NHWC"))

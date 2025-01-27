# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
with self.cached_session(use_gpu=use_gpu):
    t = constant_op.constant(1.0, shape=in_size)
    with self.assertRaisesRegex(errors_impl.UnimplementedError, error_msg):
        t = nn_ops.max_pool(
            t, ksize=ksize, strides=strides, padding="SAME").eval()

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/nn_ops/pooling_ops_test.py
with self.session(use_gpu=test.is_gpu_available()) as sess:
    pool_funcs = [nn_ops.max_pool, nn_ops.avg_pool]
    if test.is_gpu_available():
        pool_funcs.append(nn_ops.max_pool_with_argmax)
    for pool_func in pool_funcs:
        if pool_func != nn_ops.max_pool:
            # Illegal strides.
            with self.assertRaisesRegex(
                errors_impl.UnimplementedError,
                "Pooling is not yet supported on the batch"):
                sess.run(
                    pool_func(
                        array_ops.placeholder(dtypes.float32),
                        ksize=[1, 1, 1, 1],
                        strides=[2, 1, 1, 1],
                        padding="SAME"))

        # Filter too large.
        with self.assertRaisesRegex(ValueError, "Negative dimension size"):
            sess.run(
                pool_func(
                    array_ops.placeholder(dtypes.float32, shape=[32, 20, 20, 3]),
                    ksize=[1, 20, 21, 1],
                    strides=[1, 1, 1, 1],
                    padding="VALID"))
        with self.assertRaisesRegex(ValueError, "Negative dimension size"):
            pool_func(
                array_ops.placeholder(dtypes.float32, shape=[32, 20, 20, 3]),
                ksize=[1, 21, 20, 1],
                strides=[1, 1, 1, 1],
                padding="VALID")

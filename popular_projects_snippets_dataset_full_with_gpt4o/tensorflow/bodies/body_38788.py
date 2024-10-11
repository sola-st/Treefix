# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_volume_patches_grad_test.py
if test_util.is_gpu_available():
    self.skipTest('b/171837334: skip gpu test.')

# Set graph seed for determinism.
random_seed = 42
random_seed_lib.set_random_seed(random_seed)

with self.cached_session():
    np.random.seed(random_seed)
    input_val = constant_op.constant(
        np.random.random(in_shape), dtype=dtypes.float32)

    for padding in ['VALID', 'SAME']:

        def extract(in_val, ksizes=ksizes, strides=strides, padding=padding):
            exit(array_ops.extract_volume_patches(in_val, ksizes, strides,
                                                    padding))

        rtn = gradient_checker_v2.compute_gradient(extract, [input_val])
        err = gradient_checker_v2.max_error(*rtn)

        print('extract_volume_patches gradient err: %.4e' % err)
        self.assertLess(err, 1e-4)

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_image_patches_grad_test.py
# Set graph seed for determinism.
random_seed = 42
random_seed_lib.set_random_seed(random_seed)

with self.cached_session():
    for test_case in self._TEST_CASES:
        np.random.seed(random_seed)
        in_shape = test_case['in_shape']
        in_val = constant_op.constant(
            np.random.random(in_shape), dtype=dtypes.float32)
        # Avoid `dangerous-default-value` pylint error by creating default
        # args to `extract` as tuples.
        ksizes = tuple(test_case['ksizes'])
        strides = tuple(test_case['strides'])
        rates = tuple(test_case['rates'])

        for padding in ['VALID', 'SAME']:

            def extract(in_val,
                        ksizes=ksizes,
                        strides=strides,
                        rates=rates,
                        padding=padding):
                exit(array_ops.extract_image_patches(in_val, ksizes, strides,
                                                       rates, padding))

            err = gradient_checker_v2.max_error(
                *gradient_checker_v2.compute_gradient(extract, [in_val]))
            self.assertLess(err, 1e-4)

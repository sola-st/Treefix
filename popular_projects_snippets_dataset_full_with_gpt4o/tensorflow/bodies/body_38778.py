# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/image_ops/extract_image_patches_grad_test.py
"""Use test_shape_pattern to infer which dimensions are of

    variable size.
    """
# Testing shape gradient requires graph mode.
with ops.Graph().as_default():
    # Set graph seed for determinism.
    random_seed = 42
    random_seed_lib.set_random_seed(random_seed)

    with self.test_session():
        for test_case in self._TEST_CASES:
            np.random.seed(random_seed)
            in_shape = test_case['in_shape']
            test_shape = [
                x if x is None else y
                for x, y in zip(test_shape_pattern, in_shape)
            ]
            in_val = array_ops.placeholder(shape=test_shape, dtype=dtypes.float32)

            feed_dict = {in_val: np.random.random(in_shape)}
            for padding in ['VALID', 'SAME']:
                out_val = array_ops.extract_image_patches(in_val,
                                                          test_case['ksizes'],
                                                          test_case['strides'],
                                                          test_case['rates'],
                                                          padding)
                out_val_tmp = out_val.eval(feed_dict=feed_dict)
                out_shape = out_val_tmp.shape

                err = gradient_checker.compute_gradient_error(
                    in_val, in_shape, out_val, out_shape)
                self.assertLess(err, 1e-4)

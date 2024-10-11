# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
values_placeholder = array_ops.placeholder(dtype=dtypes_lib.float32)
values = _test_values((3, 2, 4, 1))
invalid_weights = (
    (1,),
    (1, 1),
    (3, 2),
    (2, 4, 1),
    (4, 2, 4, 1),
    (3, 3, 4, 1),
    (3, 2, 5, 1),
    (3, 2, 4, 2),
    (1, 1, 1, 1, 1))
expected_error_msg = 'weights can not be broadcast to values'
for invalid_weight in invalid_weights:
    # Static shapes.
    with self.assertRaisesRegex(ValueError, expected_error_msg):
        metrics.mean(values, invalid_weight)

    # Dynamic shapes.
    with self.assertRaisesRegex(errors_impl.OpError, expected_error_msg):
        with self.cached_session():
            _, update_op = metrics.mean(values_placeholder, invalid_weight)
            variables.local_variables_initializer().run()
            update_op.eval(feed_dict={values_placeholder: values})

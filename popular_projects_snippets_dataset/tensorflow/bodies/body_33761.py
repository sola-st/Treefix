# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
with ops.Graph().as_default() as g, test_case.test_session(g):
    if weights is not None:
        weights = constant_op.constant(weights, dtypes_lib.float32)
    metric, update = metrics.recall_at_k(
        predictions=constant_op.constant(predictions, dtypes_lib.float32),
        labels=labels,
        k=k,
        class_id=class_id,
        weights=weights)

    # Fails without initialized vars.
    test_case.assertRaises(errors_impl.OpError, metric.eval)
    test_case.assertRaises(errors_impl.OpError, update.eval)
    variables.variables_initializer(variables.local_variables()).run()

    # Run per-step op and assert expected values.
    if math.isnan(expected):
        _assert_nan(test_case, update.eval())
        _assert_nan(test_case, metric.eval())
    else:
        test_case.assertEqual(expected, update.eval())
        test_case.assertEqual(expected, metric.eval())

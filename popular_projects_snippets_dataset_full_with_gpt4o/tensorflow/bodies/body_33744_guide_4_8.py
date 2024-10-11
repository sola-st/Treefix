import math # pragma: no cover

test_case = type('MockTestCase', (object,), { # pragma: no cover
    'test_session': lambda self, graph: tf.compat.v1.Session(graph=graph).__enter__(), # pragma: no cover
    'assertRaises': lambda self, exp, call: (lambda: (call(), '')[1])() if not any([(hasattr(call, 'assertRaises') and call.assertRaises(exp, call)), (hasattr(tf.compat.v1.errors, 'OpError') and isinstance(call, tf.compat.v1.errors.OpError))]) else None, # pragma: no cover
    'assertTrue': lambda self, expr: (lambda: (expr, '')[1])() if expr else AssertionError(f'{expr} is not True'), # pragma: no cover
    'assertEqual': lambda self, a, b: (lambda: (a == b, '')[1])() if a == b else AssertionError(f'{a} != {b}') # pragma: no cover
})() # pragma: no cover
predictions_idx = [2, 0, 1] # pragma: no cover
k = 1 # pragma: no cover
class_id = None # pragma: no cover
weights = [0.1, 0.2, 0.7] # pragma: no cover
expected = 1.0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
from l3.Runtime import _l_
with ops.Graph().as_default() as g, test_case.test_session(g):
    _l_(22406)

    if weights is not None:
        _l_(22396)

        weights = constant_op.constant(weights, dtypes_lib.float32)
        _l_(22395)
    metric, update = metrics.precision_at_top_k(
        predictions_idx=constant_op.constant(predictions_idx, dtypes_lib.int32),
        labels=labels,
        k=k,
        class_id=class_id,
        weights=weights)
    _l_(22397)

    # Fails without initialized vars.
    test_case.assertRaises(errors_impl.OpError, metric.eval)
    _l_(22398)
    test_case.assertRaises(errors_impl.OpError, update.eval)
    _l_(22399)
    variables.variables_initializer(variables.local_variables()).run()
    _l_(22400)

    # Run per-step op and assert expected values.
    if math.isnan(expected):
        _l_(22405)

        test_case.assertTrue(math.isnan(update.eval()))
        _l_(22401)
        test_case.assertTrue(math.isnan(metric.eval()))
        _l_(22402)
    else:
        test_case.assertEqual(expected, update.eval())
        _l_(22403)
        test_case.assertEqual(expected, metric.eval())
        _l_(22404)

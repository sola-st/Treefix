import math # pragma: no cover

class TestCase: # pragma: no cover
    def test_session(self, g): # pragma: no cover
        return tf.compat.v1.Session(graph=g) # pragma: no cover
    def assertRaises(self, error, func): # pragma: no cover
        try: # pragma: no cover
            func() # pragma: no cover
        except error: # pragma: no cover
            return # pragma: no cover
        except Exception as e: # pragma: no cover
            raise AssertionError(f"Expected {error}, got {type(e)}") # pragma: no cover
        raise AssertionError(f"Expected {error.__name__} but no exception was raised") # pragma: no cover
    def assertTrue(self, expr): # pragma: no cover
        assert expr, f"{expr} is not true" # pragma: no cover
    def assertEqual(self, a, b): # pragma: no cover
        assert a == b, f"{a} != {b}" # pragma: no cover
 # pragma: no cover
test_case = TestCase() # pragma: no cover
predictions_idx = [[0, 1], [2, 3]] # pragma: no cover
k = 1 # pragma: no cover
class_id = None # pragma: no cover
weights = None # pragma: no cover
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

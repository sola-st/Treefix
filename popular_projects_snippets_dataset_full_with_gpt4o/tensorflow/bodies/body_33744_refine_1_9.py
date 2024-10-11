import math # pragma: no cover

weights = [0.25, 0.75, 1.0] if 'weights' is not None else None # pragma: no cover
predictions_idx = [1, 2, 0] # pragma: no cover
k = 2 # pragma: no cover
class_id = 1 # pragma: no cover
expected = 0.75 # pragma: no cover
math = type('Mock', (object,), {'isnan': math.isnan})() # pragma: no cover

import math # pragma: no cover
import numpy as np # pragma: no cover

class MockTestCase: # pragma: no cover
    def test_session(self, graph): # pragma: no cover
        return tf.compat.v1.Session(graph=graph) # pragma: no cover
    def assertRaises(self, error, func, *args, **kwargs): # pragma: no cover
        try: # pragma: no cover
            func(*args, **kwargs) # pragma: no cover
        except error: # pragma: no cover
            print('Raised expected exception:', error.__name__) # pragma: no cover
    def assertTrue(self, expr): # pragma: no cover
        assert expr, 'Expression is not True' # pragma: no cover
    def assertEqual(self, first, second): # pragma: no cover
        assert first == second, f'{first} != {second}' # pragma: no cover
test_case = MockTestCase() # pragma: no cover
weights = np.array([1.0, 2.0, 3.0], dtype=np.float32) # pragma: no cover
predictions_idx = np.array([[1, 0, 0], [0, 1, 0]], dtype=np.int32) # pragma: no cover
labels = np.array([[0, 1, 0], [1, 0, 0]], dtype=np.int32) # pragma: no cover
k = 1 # pragma: no cover
class_id = None # pragma: no cover
math = math # pragma: no cover
expected = 0.5 # pragma: no cover

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

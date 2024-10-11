import math # pragma: no cover

weights = [1.0, 2.0, 3.0] # pragma: no cover
predictions_idx = [1, 0, 1] # pragma: no cover
labels = [1, 0, 1] # pragma: no cover
k = 2 # pragma: no cover
class_id = 1 # pragma: no cover
expected = 0.5 # pragma: no cover

import numpy as np # pragma: no cover
import math # pragma: no cover

weights = np.array([1.0, 0.5, 0.0], dtype=np.float32) # pragma: no cover
predictions_idx = np.array([0, 1, 1, 0], dtype=np.int32) # pragma: no cover
labels = np.array([1, 0, 1, 1], dtype=np.int32) # pragma: no cover
k = 2 # pragma: no cover
class_id = 1 # pragma: no cover
expected = 1.0 # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
from l3.Runtime import _l_
with ops.Graph().as_default() as g, test_case.test_session(g):
    _l_(10113)

    if weights is not None:
        _l_(10103)

        weights = constant_op.constant(weights, dtypes_lib.float32)
        _l_(10102)
    metric, update = metrics.precision_at_top_k(
        predictions_idx=constant_op.constant(predictions_idx, dtypes_lib.int32),
        labels=labels,
        k=k,
        class_id=class_id,
        weights=weights)
    _l_(10104)

    # Fails without initialized vars.
    test_case.assertRaises(errors_impl.OpError, metric.eval)
    _l_(10105)
    test_case.assertRaises(errors_impl.OpError, update.eval)
    _l_(10106)
    variables.variables_initializer(variables.local_variables()).run()
    _l_(10107)

    # Run per-step op and assert expected values.
    if math.isnan(expected):
        _l_(10112)

        test_case.assertTrue(math.isnan(update.eval()))
        _l_(10108)
        test_case.assertTrue(math.isnan(metric.eval()))
        _l_(10109)
    else:
        test_case.assertEqual(expected, update.eval())
        _l_(10110)
        test_case.assertEqual(expected, metric.eval())
        _l_(10111)

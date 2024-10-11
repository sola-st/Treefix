class MockMetrics(object): # pragma: no cover
    def true_positives(self, labels, predictions): # pragma: no cover
        return 7, None  # Simplified for the mock behavior # pragma: no cover
metrics = MockMetrics() # pragma: no cover
class MockSelf(object): # pragma: no cover
    def cached_session(self): # pragma: no cover
        return self # pragma: no cover
    def evaluate(self, *args): # pragma: no cover
        pass # pragma: no cover
    def assertAllClose(self, a, b): # pragma: no cover
        assert abs(a - b) < 1e-6, f'Assertion failed: {a} is not close to {b}' # pragma: no cover
self = MockSelf() # pragma: no cover
class MockVariables(object): # pragma: no cover
    @staticmethod # pragma: no cover
    def local_variables_initializer(): # pragma: no cover
        pass # pragma: no cover
variables = MockVariables() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/metrics_test.py
from l3.Runtime import _l_
labels = constant_op.constant(((0, 1, 0, 1, 0),
                               (0, 0, 1, 1, 1),
                               (1, 1, 1, 1, 0),
                               (0, 0, 0, 0, 1)))
_l_(5668)
predictions = constant_op.constant(((0, 0, 1, 1, 0),
                                    (1, 1, 1, 1, 1),
                                    (0, 1, 0, 1, 0),
                                    (1, 1, 1, 1, 1)))
_l_(5669)
tn, tn_update_op = metrics.true_positives(
    labels=labels, predictions=predictions)
_l_(5670)

with self.cached_session():
    _l_(5675)

    self.evaluate(variables.local_variables_initializer())
    _l_(5671)
    self.assertAllClose(0., tn)
    _l_(5672)
    self.assertAllClose(7., tn_update_op)
    _l_(5673)
    self.assertAllClose(7., tn)
    _l_(5674)

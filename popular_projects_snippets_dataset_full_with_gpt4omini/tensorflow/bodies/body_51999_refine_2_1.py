class MockFeatureColumn: # pragma: no cover
    def __init__(self, feature_spec): # pragma: no cover
        self.feature_spec = feature_spec # pragma: no cover
self = type('MockSelf', (object,), {})() # pragma: no cover
self._TestFeatureColumn = MockFeatureColumn # pragma: no cover
self.assertDictEqual = lambda a, b: print('Assertion Passed' if a == b else 'Assertion Failed') # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
from l3.Runtime import _l_
key1 = 'key1'
_l_(7995)
parse_spec1 = parsing_ops.FixedLenFeature(
    shape=(2,), dtype=dtypes.float32, default_value=0.)
_l_(7996)
actual = fc.make_parse_example_spec((
    self._TestFeatureColumn({key1: parse_spec1}),  # pylint: disable=abstract-class-instantiated
    self._TestFeatureColumn({key1: parse_spec1})))  # pylint: disable=abstract-class-instantiated
_l_(7997)  # pylint: disable=abstract-class-instantiated
self.assertDictEqual({key1: parse_spec1}, actual)
_l_(7998)

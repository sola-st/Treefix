import unittest # pragma: no cover

class MockTestCase(unittest.TestCase): # pragma: no cover
    def _TestFeatureColumn(self, feature_spec): # pragma: no cover
        return feature_spec # pragma: no cover
self = MockTestCase() # pragma: no cover

class MockFeatureColumn(object): # pragma: no cover
    def __init__(self, feature_spec): # pragma: no cover
        self.feature_spec = feature_spec # pragma: no cover
    def get_feature_spec(self): return self.feature_spec # pragma: no cover
self = type('Mock', (object,), {'_TestFeatureColumn': MockFeatureColumn, 'assertDictEqual': lambda self, a, b: a == b})() # pragma: no cover
parsing_ops = type('parsing_ops', (object,), {'FixedLenFeature': lambda shape, dtype, default_value: {'shape': shape, 'dtype': dtype, 'default_value': default_value}})() # pragma: no cover

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

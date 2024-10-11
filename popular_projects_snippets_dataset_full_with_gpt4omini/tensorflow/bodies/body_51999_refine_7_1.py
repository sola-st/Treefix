fc = type('Mock', (object,), {'make_parse_example_spec': lambda self, spec: spec})() # pragma: no cover
self = type('Mock', (object,), {'_TestFeatureColumn': lambda self, spec: spec, 'assertDictEqual': lambda self, dict1, dict2: dict1 == dict2})() # pragma: no cover

class Mock: pass# pragma: no cover
self = Mock() # pragma: no cover
self._TestFeatureColumn = lambda feature_spec: feature_spec # pragma: no cover
self.assertDictEqual = lambda a, b: a == b # pragma: no cover

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

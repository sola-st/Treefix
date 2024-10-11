self = type('Mock', (object,), {'_TestFeatureColumn': lambda self, args: list(args.values())[0], 'assertDictEqual': lambda self, x, y: None})() # pragma: no cover

self = type('Mock', (object,), {'_TestFeatureColumn': lambda self, args: list(args.values())[0], 'assertDictEqual': lambda self, x, y: None})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_test.py
from l3.Runtime import _l_
key1 = 'key1'
_l_(21153)
parse_spec1 = parsing_ops.FixedLenFeature(
    shape=(2,), dtype=dtypes.float32, default_value=0.)
_l_(21154)
actual = fc.make_parse_example_spec((
    self._TestFeatureColumn({key1: parse_spec1}),  # pylint: disable=abstract-class-instantiated
    self._TestFeatureColumn({key1: parse_spec1})))  # pylint: disable=abstract-class-instantiated
_l_(21155)  # pylint: disable=abstract-class-instantiated
self.assertDictEqual({key1: parse_spec1}, actual)
_l_(21156)

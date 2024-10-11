parsing_ops = type('parsing_ops', (object,), {'FixedLenFeature': lambda shape, dtype, default_value: {'shape': shape, 'dtype': dtype, 'default_value': default_value}}) # pragma: no cover
fc = type('fc', (object,), {'make_parse_example_spec': lambda features: {k: v for f in features for k, v in f.items()}}) # pragma: no cover
self = type('self', (object,), {'_TestFeatureColumn': lambda feature: feature, 'assertDictEqual': lambda self, a, b: a == b}) # pragma: no cover

self = type('MockSelf', (object,), { # pragma: no cover
    '_TestFeatureColumn': lambda self, feature_dict: feature_dict, # pragma: no cover
    'assertDictEqual': lambda self, dict1, dict2: (dict1 == dict2) # pragma: no cover
})() # pragma: no cover

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

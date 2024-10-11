import unittest # pragma: no cover

class TestNumericColumn(unittest.TestCase): # pragma: no cover
    def test_numeric_column_shape(self): # pragma: no cover
        with self.assertRaisesRegex(TypeError, 'shape dimensions must be integer'): # pragma: no cover
            fc.numeric_column('aaa', shape=[1.0]) # pragma: no cover
        with self.assertRaisesRegex(ValueError, 'shape dimensions must be greater than 0'): # pragma: no cover
            fc.numeric_column('aaa', shape=[0]) # pragma: no cover
        unittest.main() # pragma: no cover
type('Mock', (object,), {'assertRaisesRegex': unittest.TestCase.assertRaisesRegex}) # pragma: no cover
self = type('Mock', (object,), {'assertRaisesRegex': unittest.TestCase.assertRaisesRegex})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
from l3.Runtime import _l_
with self.assertRaisesRegex(TypeError, 'shape dimensions must be integer'):
    _l_(21501)

    fc.numeric_column(
        'aaa', shape=[
            1.0,
        ])
    _l_(21500)

with self.assertRaisesRegex(ValueError,
                            'shape dimensions must be greater than 0'):
    _l_(21503)

    fc.numeric_column(
        'aaa', shape=[
            0,
        ])
    _l_(21502)

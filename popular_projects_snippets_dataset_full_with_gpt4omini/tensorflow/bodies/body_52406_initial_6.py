class TestClass:  # Mock class for testing# pragma: no cover
    def assertRaisesRegex(self, exception, regex):# pragma: no cover
        return self # pragma: no cover
self = TestClass() # pragma: no cover
class MockFC:# pragma: no cover
    def numeric_column(self, name, shape):# pragma: no cover
        if isinstance(shape[0], float):# pragma: no cover
            raise TypeError('shape dimensions must be integer')# pragma: no cover
        if shape[0] <= 0:# pragma: no cover
            raise ValueError('shape dimensions must be greater than 0') # pragma: no cover
fc = MockFC() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/feature_column/feature_column_v2_test.py
from l3.Runtime import _l_
with self.assertRaisesRegex(TypeError, 'shape dimensions must be integer'):
    _l_(9209)

    fc.numeric_column(
        'aaa', shape=[
            1.0,
        ])
    _l_(9208)

with self.assertRaisesRegex(ValueError,
                            'shape dimensions must be greater than 0'):
    _l_(9211)

    fc.numeric_column(
        'aaa', shape=[
            0,
        ])
    _l_(9210)

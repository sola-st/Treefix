from unittest.mock import Mock # pragma: no cover

self = Mock() # pragma: no cover
self.assertRaisesRegex = Mock() # pragma: no cover
fc = Mock() # pragma: no cover
fc.numeric_column = Mock() # pragma: no cover

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

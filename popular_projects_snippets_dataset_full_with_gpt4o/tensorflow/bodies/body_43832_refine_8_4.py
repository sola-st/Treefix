from typing import List # pragma: no cover
import unittest # pragma: no cover

type_ = int # pragma: no cover
_int_dataset = int # pragma: no cover
xla = True # pragma: no cover
self = type('Mock', (object,), {'skipTest': lambda self, msg: None, 'assertFunctionMatchesEager': lambda self, func, var, xla: None})() # pragma: no cover
_int_tensor = int # pragma: no cover
l = [1, 2, 3] # pragma: no cover
for_two_vars = lambda x, y: (x + y, x - y) # pragma: no cover

import unittest # pragma: no cover

type_ = list # pragma: no cover
_int_dataset = list # pragma: no cover
xla = True # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
from l3.Runtime import _l_
if type_ is _int_dataset and xla:
    _l_(22156)

    self.skipTest('Datsets not supported in XLA')
    _l_(22155)
if type_ is _int_tensor and xla and not l:
    _l_(22158)

    self.skipTest('Empty loops not supported in XLA')
    _l_(22157)

l = type_(l)
_l_(22159)
self.assertFunctionMatchesEager(for_two_vars, l, xla=xla)
_l_(22160)

import unittest # pragma: no cover
import torch # pragma: no cover
import typing # pragma: no cover

class MockTest(unittest.TestCase): # pragma: no cover
    def skipTest(self, reason): # pragma: no cover
        print(f'Skip test: {reason}') # pragma: no cover
 # pragma: no cover
    def assertFunctionMatchesEager(self, func, l, xla): # pragma: no cover
        print(f'Function {func.__name__} matches for {l} with XLA={xla}') # pragma: no cover
 # pragma: no cover
def for_two_vars(l): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
_int_dataset = list # pragma: no cover
_int_tensor = torch.Tensor # pragma: no cover
type_ = _int_tensor # pragma: no cover
xla = True # pragma: no cover
l = [] # pragma: no cover
 # pragma: no cover
self = MockTest() # pragma: no cover

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

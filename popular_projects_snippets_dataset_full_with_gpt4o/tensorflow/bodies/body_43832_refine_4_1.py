from unittest import TestCase, skip # pragma: no cover
import numpy as np # pragma: no cover
import torch # pragma: no cover

type_ = int # pragma: no cover
_int_dataset = list # pragma: no cover
xla = False # pragma: no cover
class MockTest(TestCase): # pragma: no cover
    def skipTest(self, reason): # pragma: no cover
        print(f'Test skipped: {reason}') # pragma: no cover
    def assertFunctionMatchesEager(self, func, *args, **kwargs): # pragma: no cover
        print('Function matches eager execution') # pragma: no cover
self = MockTest() # pragma: no cover
_int_tensor = torch.Tensor # pragma: no cover
l = [1, 2, 3] # pragma: no cover
def for_two_vars(a, b): # pragma: no cover
    return a + b # pragma: no cover

from unittest import TestCase, skip # pragma: no cover

type_ = list # pragma: no cover
_int_dataset = list # pragma: no cover
_int_tensor = list # pragma: no cover
xla = False # pragma: no cover
l = [1, 2, 3] # pragma: no cover
def for_two_vars(a, b): return a + b # pragma: no cover
class MockTest(TestCase):# pragma: no cover
    def skipTest(self, reason):# pragma: no cover
        print(f'Test skipped: {reason}')# pragma: no cover
    def assertFunctionMatchesEager(self, func, *args, **kwargs):# pragma: no cover
        print('Function matches eager execution') # pragma: no cover
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

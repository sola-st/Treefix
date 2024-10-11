import unittest # pragma: no cover
import torch # pragma: no cover

class MockTest(unittest.TestCase): # pragma: no cover
    def skipTest(self, reason): # pragma: no cover
        print(f'Skipped: {reason}') # pragma: no cover
 # pragma: no cover
def _int_dataset(lst): # pragma: no cover
    return torch.tensor(lst) # pragma: no cover
 # pragma: no cover
def _int_tensor(lst): # pragma: no cover
    return torch.tensor(lst) # pragma: no cover
 # pragma: no cover
def for_two_vars(tensor, xla=False): # pragma: no cover
    pass # pragma: no cover
 # pragma: no cover
test_instance = MockTest('skipTest') # pragma: no cover

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

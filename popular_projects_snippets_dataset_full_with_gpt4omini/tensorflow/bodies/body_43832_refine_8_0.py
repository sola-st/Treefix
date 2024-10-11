import numpy as np # pragma: no cover

xla = True # pragma: no cover
self = type('Mock', (object,), {'skipTest': lambda self, msg: print(f'Skipped: {msg}'), 'assertFunctionMatchesEager': lambda self, func, result, xla: print(f'Asserted function matches eager: {func}, {result}, xla={xla}')})() # pragma: no cover
for_two_vars = lambda a, b: a + b # pragma: no cover

import numpy as np # pragma: no cover

xla = True # pragma: no cover
self = type('Mock', (object,), {'skipTest': lambda self, msg: print('Skipped:', msg), 'assertFunctionMatchesEager': lambda self, func, arg, xla: print('Function matches eager execution with xla=', xla)})() # pragma: no cover
for_two_vars = lambda a, b: a + b # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/tests/loop_basic_test.py
from l3.Runtime import _l_
if type_ is _int_dataset and xla:
    _l_(9848)

    self.skipTest('Datsets not supported in XLA')
    _l_(9847)
if type_ is _int_tensor and xla and not l:
    _l_(9850)

    self.skipTest('Empty loops not supported in XLA')
    _l_(9849)

l = type_(l)
_l_(9851)
self.assertFunctionMatchesEager(for_two_vars, l, xla=xla)
_l_(9852)

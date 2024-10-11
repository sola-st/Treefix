import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

tm = type('Mock', (object,), {'makeCustomDataframe': lambda self, rows, cols, data_gen_f, c_idx_type, r_idx_type: pd.DataFrame(np.arange(rows * cols).reshape(rows, cols), columns=pd.Index(['C1', 'C2'], name=c_idx_type), index=pd.Index([0, 1], name=r_idx_type)), 'assert_frame_equal': pd.testing.assert_frame_equal})() # pragma: no cover
f = lambda r, c: np.arange(r * c).reshape(r, c) # pragma: no cover
self = type('Mock', (object,), {'eval': lambda self, expr, local_dict: eval(expr, {}, local_dict)})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
from l3.Runtime import _l_
df = tm.makeCustomDataframe(2, 2, data_gen_f=f, c_idx_type="p", r_idx_type="i")
_l_(20948)

e = df < 2
_l_(20949)
r = self.eval("df < 2", local_dict={"df": df})
_l_(20950)
x = df < 2
_l_(20951)

tm.assert_frame_equal(r, e)
_l_(20952)
tm.assert_frame_equal(x, e)
_l_(20953)

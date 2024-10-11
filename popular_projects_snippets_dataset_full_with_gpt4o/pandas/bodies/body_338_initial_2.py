import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

class MockTM: # pragma: no cover
    @staticmethod # pragma: no cover
    def makeCustomDataframe(rows, cols, data_gen_f, c_idx_type, r_idx_type): # pragma: no cover
        idx = pd.Index([data_gen_f() for _ in range(rows)], name=r_idx_type) # pragma: no cover
        cols = pd.Index([c_idx_type + str(i) for i in range(cols)], name=c_idx_type) # pragma: no cover
        data = np.array([[data_gen_f() for _ in range(cols)] for _ in range(rows)]) # pragma: no cover
        return pd.DataFrame(data, index=idx, columns=cols) # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_frame_equal(df1, df2): # pragma: no cover
        pd.testing.assert_frame_equal(df1, df2) # pragma: no cover
tm = MockTM() # pragma: no cover
 # pragma: no cover
def f(): # pragma: no cover
    return 1 # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    @staticmethod # pragma: no cover
    def eval(expr, local_dict): # pragma: no cover
        return eval(expr, {}, local_dict) # pragma: no cover
self = MockSelf() # pragma: no cover

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

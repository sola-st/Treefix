import pandas as pd # pragma: no cover

class MockTM: # pragma: no cover
    @staticmethod # pragma: no cover
    def makeCustomDataframe(rows, cols, data_gen_f, c_idx_type, r_idx_type): # pragma: no cover
        data = data_gen_f(rows * cols) # pragma: no cover
        return pd.DataFrame(data.reshape(rows, cols), columns=[c_idx_type + str(i) for i in range(cols)], index=[r_idx_type + str(i) for i in range(rows)]) # pragma: no cover
 # pragma: no cover
    @staticmethod # pragma: no cover
    def assert_frame_equal(result, expected): # pragma: no cover
        pd.testing.assert_frame_equal(result, expected) # pragma: no cover
 # pragma: no cover
class MockSelf: # pragma: no cover
    @staticmethod # pragma: no cover
    def eval(expression, local_dict): # pragma: no cover
        return eval(expression, {}, local_dict) # pragma: no cover
 # pragma: no cover
tm = MockTM() # pragma: no cover
f = lambda n: [i for i in range(n)] # pragma: no cover
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

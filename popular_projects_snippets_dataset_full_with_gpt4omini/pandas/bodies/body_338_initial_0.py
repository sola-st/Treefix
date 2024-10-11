import pandas as pd # pragma: no cover
import numpy as np # pragma: no cover

class Mock: pass # pragma: no cover
tm = Mock() # pragma: no cover
def makeCustomDataframe(rows, cols, data_gen_f, c_idx_type, r_idx_type): # pragma: no cover
    data = data_gen_f(rows, cols) # pragma: no cover
    index = pd.Index(range(rows), name='i') # pragma: no cover
    columns = pd.Index([f'p{col}' for col in range(cols)], name='p') # pragma: no cover
    return pd.DataFrame(data, index=index, columns=columns) # pragma: no cover
tm.makeCustomDataframe = makeCustomDataframe # pragma: no cover
def f(rows, cols): # pragma: no cover
    return np.random.randint(0, 5, size=(rows, cols)) # pragma: no cover
self = Mock() # pragma: no cover
def eval(expression, local_dict): # pragma: no cover
    df = local_dict['df'] # pragma: no cover
    return df < 2 # pragma: no cover
self.eval = eval # pragma: no cover
def assert_frame_equal(left, right): # pragma: no cover
    pd.testing.assert_frame_equal(left, right) # pragma: no cover
tm.assert_frame_equal = assert_frame_equal # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
from l3.Runtime import _l_
df = tm.makeCustomDataframe(2, 2, data_gen_f=f, c_idx_type="p", r_idx_type="i")
_l_(9892)

e = df < 2
_l_(9893)
r = self.eval("df < 2", local_dict={"df": df})
_l_(9894)
x = df < 2
_l_(9895)

tm.assert_frame_equal(r, e)
_l_(9896)
tm.assert_frame_equal(x, e)
_l_(9897)

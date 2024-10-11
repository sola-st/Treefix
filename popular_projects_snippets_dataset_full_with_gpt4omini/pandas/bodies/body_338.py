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

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/computation/test_eval.py
from l3.Runtime import _l_
df = DataFrame(np.random.randn(5, 2), columns=list("ab"))
_l_(10327)
# single assignment - new variable
expected = df.copy()
_l_(10328)
expected["c"] = expected["a"] + expected["b"]
_l_(10329)
df.eval("c = a + b", inplace=True)
_l_(10330)
tm.assert_frame_equal(df, expected)
_l_(10331)

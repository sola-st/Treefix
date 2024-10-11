import pandas as pd # pragma: no cover
import pandas._testing as tm # pragma: no cover

DataFrame = pd.DataFrame # pragma: no cover
tm = type('Mock', (object,), {'assert_frame_equal': tm.assert_frame_equal})() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# related #2305

from l3.Runtime import _l_
gen1 = (i for i in range(10))
_l_(19663)
gen2 = (i for i in range(10))
_l_(19664)

expected = DataFrame([list(range(10)), list(range(10))])
_l_(19665)
result = DataFrame([gen1, gen2])
_l_(19666)
tm.assert_frame_equal(result, expected)
_l_(19667)

gen = ([i, "a"] for i in range(10))
_l_(19668)
result = DataFrame(gen)
_l_(19669)
expected = DataFrame({0: range(10), 1: "a"})
_l_(19670)
tm.assert_frame_equal(result, expected, check_dtype=False)
_l_(19671)

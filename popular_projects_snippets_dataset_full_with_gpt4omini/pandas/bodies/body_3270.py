# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# preserver the timedelta conversion
# GH#19223
from l3.Runtime import _l_
dtype = f"m8[{unit}]"
_l_(9955)
arr = np.array([[1, 2, 3]], dtype=dtype)
_l_(9956)
df = DataFrame(arr)
_l_(9957)
result = df.astype(dtype)
_l_(9958)
expected = DataFrame(arr.astype(dtype))
_l_(9959)

tm.assert_frame_equal(result, expected)
_l_(9960)

# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
scalar = cls("NaT", "ns")
dtype = {np.datetime64: "m8[ns]", np.timedelta64: "M8[ns]"}[cls]

if cls is np.datetime64:
    msg1 = r"dtype datetime64\[ns\] cannot be converted to timedelta64\[ns\]"
else:
    msg1 = r"dtype timedelta64\[ns\] cannot be converted to datetime64\[ns\]"
msg = "|".join(["Cannot cast", msg1])

with pytest.raises(TypeError, match=msg):
    constructor(scalar, dtype=dtype)

scalar = cls(4, "ns")
with pytest.raises(TypeError, match=msg):
    constructor(scalar, dtype=dtype)

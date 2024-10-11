# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# trying to astype a m to a M, or vice-versa
# GH#19224
dtype = f"M8[{unit}]"
other = f"m8[{unit}]"

df = DataFrame(np.array([[1, 2, 3]], dtype=dtype))
msg = "|".join(
    [
        # BlockManager path
        rf"Cannot cast DatetimeArray to dtype timedelta64\[{unit}\]",
        # ArrayManager path
        "cannot astype a datetimelike from "
        rf"\[datetime64\[ns\]\] to \[timedelta64\[{unit}\]\]",
    ]
)
with pytest.raises(TypeError, match=msg):
    df.astype(other)

msg = "|".join(
    [
        # BlockManager path
        rf"Cannot cast TimedeltaArray to dtype datetime64\[{unit}\]",
        # ArrayManager path
        "cannot astype a timedelta from "
        rf"\[timedelta64\[ns\]\] to \[datetime64\[{unit}\]\]",
    ]
)
df = DataFrame(np.array([[1, 2, 3]], dtype=other))
with pytest.raises(TypeError, match=msg):
    df.astype(dtype)

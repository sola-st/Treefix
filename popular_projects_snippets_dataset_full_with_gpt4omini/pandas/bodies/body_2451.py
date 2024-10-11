# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#44514 don't cast mismatched nulls to pd.NA
df = DataFrame({"A": [1, 2, 3]}, dtype=any_numeric_ea_dtype)
ser = df["A"]
arr = ser._values

msg = "|".join(
    [
        r"timedelta64\[ns\] cannot be converted to (Floating|Integer)Dtype",
        r"datetime64\[ns\] cannot be converted to (Floating|Integer)Dtype",
        "'values' contains non-numeric NA",
        r"Invalid value '.*' for dtype (U?Int|Float)\d{1,2}",
    ]
)
with pytest.raises(TypeError, match=msg):
    arr[0] = null

with pytest.raises(TypeError, match=msg):
    arr[:2] = [null, null]

with pytest.raises(TypeError, match=msg):
    ser[0] = null

with pytest.raises(TypeError, match=msg):
    ser[:2] = [null, null]

with pytest.raises(TypeError, match=msg):
    ser.iloc[0] = null

with pytest.raises(TypeError, match=msg):
    ser.iloc[:2] = [null, null]

with pytest.raises(TypeError, match=msg):
    df.iloc[0, 0] = null

with pytest.raises(TypeError, match=msg):
    df.iloc[:2, 0] = [null, null]

# Multi-Block
df2 = df.copy()
df2["B"] = ser.copy()
with pytest.raises(TypeError, match=msg):
    df2.iloc[0, 0] = null

with pytest.raises(TypeError, match=msg):
    df2.iloc[:2, 0] = [null, null]

# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_astype.py
# tests astype to object dtype
# GH#19223 / GH#12425
dtype = f"{dtype}[{unit}]"
arr = np.array([[1, 2, 3]], dtype=dtype)
df = DataFrame(arr)
result = df.astype(object)
assert (result.dtypes == object).all()

if dtype.startswith("M8"):
    assert result.iloc[0, 0] == Timestamp(1, unit=unit)
else:
    assert result.iloc[0, 0] == Timedelta(1, unit=unit)

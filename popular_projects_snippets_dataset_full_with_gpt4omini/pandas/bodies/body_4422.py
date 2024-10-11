# Extracted from ./data/repos/pandas/pandas/tests/frame/test_constructors.py
# Ensure constructor honors dtype
data = np.ma.array(
    np.ma.zeros(5, dtype=[("date", "<f8"), ("price", "<f8")]), mask=[False] * 5
)
data = data.view(mrecords.mrecarray)
with pytest.raises(TypeError, match=r"Pass \{name: data\[name\]"):
    # Support for MaskedRecords deprecated GH#40363
    DataFrame(data, dtype=int)

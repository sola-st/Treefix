# Extracted from ./data/repos/pandas/pandas/tests/io/excel/test_writers.py
# GH 27008, GH 7056
tz = tz_aware_fixture
data = pd.Timestamp("2019", tz=tz)
df = DataFrame([data], dtype=dtype)
with pytest.raises(ValueError, match="Excel does not support"):
    df.to_excel(path)

data = data.to_pydatetime()
df = DataFrame([data], dtype=dtype)
with pytest.raises(ValueError, match="Excel does not support"):
    df.to_excel(path)

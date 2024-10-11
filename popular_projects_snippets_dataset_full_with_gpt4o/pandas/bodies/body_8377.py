# Extracted from ./data/repos/pandas/pandas/tests/indexes/datetimes/test_date_range.py
# GH#11587
msg = "Neither `start` nor `end` can be NaT"
with pytest.raises(ValueError, match=msg):
    date_range(start="2016-01-01", end=pd.NaT, freq="D")
with pytest.raises(ValueError, match=msg):
    date_range(start=pd.NaT, end="2016-01-01", freq="D")

# Extracted from ./data/repos/pandas/pandas/tests/series/accessors/test_dt_accessor.py
# GH#9322 check that series with incorrect dtypes don't have attr
with pytest.raises(AttributeError, match="only use .dt accessor"):
    ser.dt
assert not hasattr(ser, "dt")

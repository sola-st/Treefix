# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_between_time.py
# GH11818
rng = date_range("1/1/2000", "1/5/2000", freq="5min")
obj = DataFrame({"A": 0}, index=rng)
obj = tm.get_obj(obj, frame_or_series)

msg = r"Cannot convert arg \[datetime\.datetime\(2010, 1, 2, 1, 0\)\] to a time"
with pytest.raises(ValueError, match=msg):
    obj.between_time(datetime(2010, 1, 2, 1), datetime(2010, 1, 2, 5))

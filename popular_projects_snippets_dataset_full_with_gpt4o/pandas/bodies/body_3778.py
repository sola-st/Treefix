# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_between_time.py
# GH#11818
rng = date_range("1/1/2000", "1/5/2000", freq="5min")
ts = DataFrame(np.random.randn(len(rng), 2), index=rng)
ts = tm.get_obj(ts, frame_or_series)

strings = [
    ("2:00", "2:30"),
    ("0200", "0230"),
    ("2:00am", "2:30am"),
    ("0200am", "0230am"),
    ("2:00:00", "2:30:00"),
    ("020000", "023000"),
    ("2:00:00am", "2:30:00am"),
    ("020000am", "023000am"),
]
expected_length = 28

for time_string in strings:
    assert len(ts.between_time(*time_string)) == expected_length

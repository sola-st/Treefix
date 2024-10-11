# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_replace.py
# GH#33340

ser = pd.Series([1, 2, "A", fixed_now_ts, True])
to_replace = {0: 1, 2: "A"}
value = "foo"
msg = "Series.replace cannot use dict-like to_replace and non-None value"
with pytest.raises(ValueError, match=msg):
    ser.replace(to_replace, value)

to_replace = 1
value = {0: "foo", 2: "bar"}
msg = "Series.replace cannot use dict-value and non-None to_replace"
with pytest.raises(ValueError, match=msg):
    ser.replace(to_replace, value)

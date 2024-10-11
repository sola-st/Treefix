# Extracted from ./data/repos/pandas/pandas/tests/indexing/interval/test_interval_new.py
# GH#27365
ser = series_with_interval_index.copy()
obj = frame_or_series(ser)
with pytest.raises(KeyError, match=r"\[6\]"):
    obj.loc[[4, 5, 6]]

# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_series_info.py
s = Series(np.random.randn(101))
msg = "Argument `max_cols` can only be passed in DataFrame.info, not Series.info"
with pytest.raises(ValueError, match=msg):
    s.info(max_cols=1)

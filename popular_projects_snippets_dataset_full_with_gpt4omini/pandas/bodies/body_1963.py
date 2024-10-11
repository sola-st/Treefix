# Extracted from ./data/repos/pandas/pandas/tests/test_register_accessor.py
# Need to restore mean
mean = pd.Series.mean
try:
    with tm.assert_produces_warning(UserWarning) as w:
        pd.api.extensions.register_series_accessor("mean")(MyAccessor)
        s = pd.Series([1, 2])
        assert s.mean.prop == "item"
    msg = str(w[0].message)
    assert "mean" in msg
    assert "MyAccessor" in msg
    assert "Series" in msg
finally:
    pd.Series.mean = mean

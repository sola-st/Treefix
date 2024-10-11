# Extracted from ./data/repos/pandas/pandas/tests/window/test_timeseries_window.py
idx = [Timestamp("2020"), NaT]
kwargs = {"columns" if axis == 1 else "index": idx}
df = DataFrame(np.eye(2), **kwargs)
with pytest.raises(ValueError, match=f"{msg} values must not have NaT"):
    df.rolling("D", axis=axis).mean()

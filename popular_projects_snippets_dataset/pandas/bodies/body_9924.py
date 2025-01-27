# Extracted from ./data/repos/pandas/pandas/tests/window/test_api.py

# ok
Series(np.ones(10)).rolling(window=3, center=True, axis=0, step=step).mean()

# bad axis
msg = "No axis named 1 for object type Series"
with pytest.raises(ValueError, match=msg):
    Series(np.ones(10)).rolling(window=3, center=True, axis=1, step=step).mean()

# ok ok
DataFrame(np.ones((10, 10))).rolling(
    window=3, center=True, axis=0, step=step
).mean()
DataFrame(np.ones((10, 10))).rolling(
    window=3, center=True, axis=1, step=step
).mean()

# bad axis
msg = "No axis named 2 for object type DataFrame"
with pytest.raises(ValueError, match=msg):
    (
        DataFrame(np.ones((10, 10)))
        .rolling(window=3, center=True, axis=2, step=step)
        .mean()
    )

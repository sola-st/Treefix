# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_align.py
df = DataFrame(np.arange(50).reshape((10, 5)))
series = Series(np.arange(5))

with pytest.raises(ValueError, match=r"axis=0 or 1"):
    df.align(series)

# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.eye(2), columns=MultiIndex.from_tuples([(0, 1), (1, 2)]))
msg = "An iterable subplots for a DataFrame with a MultiIndex"
with pytest.raises(NotImplementedError, match=msg):
    df.plot(subplots=[(0, 1)])

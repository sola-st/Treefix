# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(np.eye(2), columns=["a", "a"])
msg = "An iterable subplots for a DataFrame with non-unique"
with pytest.raises(NotImplementedError, match=msg):
    df.plot(subplots=[("a",)])

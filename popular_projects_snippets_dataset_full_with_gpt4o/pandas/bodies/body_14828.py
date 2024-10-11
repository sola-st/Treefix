# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
d = {"a": np.arange(10), "b": np.arange(10), "c": np.arange(10)}
df = DataFrame(d)

with pytest.raises(ValueError, match="should be in only one subplot"):
    df.plot(subplots=[("a", "b"), ("a", "c")])

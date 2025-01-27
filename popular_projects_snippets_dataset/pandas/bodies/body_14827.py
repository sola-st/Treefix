# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
d = {"a": np.arange(10), "b": np.arange(10)}
df = DataFrame(d)

with pytest.raises(ValueError, match=r"Column label\(s\) \['bad_name'\]"):
    df.plot(subplots=[("a", "bad_name")])

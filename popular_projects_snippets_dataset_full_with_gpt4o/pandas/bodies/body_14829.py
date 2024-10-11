# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
d = {"a": np.arange(10), "b": np.arange(10)}
df = DataFrame(d)
with pytest.raises(
    ValueError, match="When subplots is an iterable, kind must be one of"
):
    df.plot(subplots=[("a", "b")], kind=kind)

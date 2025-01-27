# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
# Make sure error is raised when subplots is not a properly
# formatted iterable. Only iterables of iterables are permitted, and
# entries should not be strings.
d = {"a": np.arange(10), "b": np.arange(10)}
df = DataFrame(d)

with pytest.raises(ValueError, match=expected_msg):
    df.plot(subplots=subplots)

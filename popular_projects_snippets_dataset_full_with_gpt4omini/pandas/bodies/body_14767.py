# Extracted from ./data/repos/pandas/pandas/tests/plotting/frame/test_frame.py
df = DataFrame(
    np.random.randn(6, 4),
    index=list(string.ascii_letters[:6]),
    columns=["one", "two", "three", "four"],
)
msg = "return_type must be {None, 'axes', 'dict', 'both'}"
with pytest.raises(ValueError, match=msg):
    df.plot.box(return_type="not_a_type")

result = df.plot.box(return_type="dict")
self._check_box_return_type(result, "dict")

result = df.plot.box(return_type="axes")
self._check_box_return_type(result, "axes")

result = df.plot.box()  # default axes
self._check_box_return_type(result, "axes")

result = df.plot.box(return_type="both")
self._check_box_return_type(result, "both")

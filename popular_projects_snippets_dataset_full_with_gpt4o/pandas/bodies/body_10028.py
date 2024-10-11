# Extracted from ./data/repos/pandas/pandas/tests/window/test_online.py
ser = Series(range(10))
kwargs = {}
if method == "aggregate":
    kwargs["func"] = lambda x: x

with pytest.raises(NotImplementedError, match=".* is not implemented."):
    getattr(ser.ewm(1).online(), method)(**kwargs)

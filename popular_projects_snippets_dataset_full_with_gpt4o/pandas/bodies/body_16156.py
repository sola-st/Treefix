# Extracted from ./data/repos/pandas/pandas/tests/series/test_reductions.py
ser = Series([1, 2])
param = list(kwargs)[0]
name = func.__name__

msg = (
    f"the '{param}' parameter is not "
    "supported in the pandas "
    rf"implementation of {name}\(\)"
)
with pytest.raises(ValueError, match=msg):
    func(ser, **kwargs)

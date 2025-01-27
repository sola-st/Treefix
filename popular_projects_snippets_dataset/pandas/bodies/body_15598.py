# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_fillna.py
ser = Series(np.random.randint(-100, 100, 50))
msg = '"value" parameter must be a scalar or dict, but you passed a "list"'
with pytest.raises(TypeError, match=msg):
    ser.fillna([1, 2])

msg = '"value" parameter must be a scalar or dict, but you passed a "tuple"'
with pytest.raises(TypeError, match=msg):
    ser.fillna((1, 2))

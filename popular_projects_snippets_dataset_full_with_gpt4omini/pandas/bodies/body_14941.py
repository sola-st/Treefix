# Extracted from ./data/repos/pandas/pandas/tests/plotting/test_converter.py
inner = [Timestamp("2017-01-01"), Timestamp("2017-01-02")]
data = [inner, inner]
result = dtc.convert(data, None, None)
expected = [dtc.convert(x, None, None) for x in data]
assert (np.array(result) == expected).all()

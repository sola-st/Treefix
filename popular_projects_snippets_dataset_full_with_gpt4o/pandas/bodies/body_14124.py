# Extracted from ./data/repos/pandas/pandas/tests/io/formats/test_format.py
s = Series(
    np.random.randn(10), index=date_range("1/1/2000", periods=10), name=0
)

result = repr(s)
assert "Freq: D, Name: 0" in result

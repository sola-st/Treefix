# Extracted from ./data/repos/pandas/pandas/tests/reductions/test_reductions.py
# See GH#16830
data = np.arange(1, 11)

s = Series(data, index=data)
result = np.argmax(s)
expected = np.argmax(data)
assert result == expected

result = s.argmax()

assert result == expected

msg = "the 'out' parameter is not supported"
with pytest.raises(ValueError, match=msg):
    np.argmax(s, out=data)

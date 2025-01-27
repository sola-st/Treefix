# Extracted from ./data/repos/pandas/pandas/tests/extension/base/getitem.py
# https://github.com/pandas-dev/pandas/pull/30175
s = pd.Series(data)
result = s[:1].item()
assert result == data[0]

msg = "can only convert an array of size 1 to a Python scalar"
with pytest.raises(ValueError, match=msg):
    s[:0].item()

with pytest.raises(ValueError, match=msg):
    s.item()

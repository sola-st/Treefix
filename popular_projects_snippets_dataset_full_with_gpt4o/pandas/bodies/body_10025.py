# Extracted from ./data/repos/pandas/pandas/tests/window/test_online.py
df = DataFrame({"a": range(5), "b": range(5)})
online_ewm = df.head(2).ewm(0.5).online()
with pytest.raises(
    ValueError,
    match="Must call mean with update=None first before passing update",
):
    online_ewm.mean(update=df.head(1))

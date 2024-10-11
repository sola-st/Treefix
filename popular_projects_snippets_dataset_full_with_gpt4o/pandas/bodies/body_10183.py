# Extracted from ./data/repos/pandas/pandas/tests/window/test_groupby.py
# GH 43909

shuffled = [3, 0, 1, 2]
sec = 1_000
df = DataFrame(
    [{"t": Timestamp(2 * x * sec), "x": x + 1, "c": 42} for x in shuffled]
)
with pytest.raises(ValueError, match=r".* must be monotonic"):
    df.groupby("c").rolling(on="t", window="3s")

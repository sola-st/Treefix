# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_sample.py
df = DataFrame({"a": [1, 2], "b": [1, 2]})
msg = "Please enter a value for `frac` OR `n`, not both"

with pytest.raises(ValueError, match=msg):
    df.groupby("a").sample(n=1, frac=1.0)

with pytest.raises(ValueError, match=msg):
    df.groupby("a")["b"].sample(n=1, frac=1.0)

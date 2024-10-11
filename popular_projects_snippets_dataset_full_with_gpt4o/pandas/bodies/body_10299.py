# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_sample.py
df = DataFrame({"a": [1, 2], "b": [1, 2]})

if n < 0:
    msg = "A negative number of rows requested. Please provide `n` >= 0."
else:
    msg = "Only integers accepted as `n` values"

with pytest.raises(ValueError, match=msg):
    df.groupby("a").sample(n=n)

with pytest.raises(ValueError, match=msg):
    df.groupby("a")["b"].sample(n=n)

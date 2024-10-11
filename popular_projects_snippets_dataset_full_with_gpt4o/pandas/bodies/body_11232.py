# Extracted from ./data/repos/pandas/pandas/tests/groupby/test_grouping.py
# related GH5375
# groupby misbehaving when using a Floatlike index
df = DataFrame(np.arange(10).reshape(5, 2), columns=list("AB"))

df.index = index(len(df))
df.groupby(list("abcde"), group_keys=False).apply(lambda x: x)

df.index = list(reversed(df.index.tolist()))
df.groupby(list("abcde"), group_keys=False).apply(lambda x: x)

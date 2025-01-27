# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py
index = [52195.504153, 52196.303147, 52198.369883]
df = DataFrame(np.random.rand(3, 2), index=index)

s1 = df.loc[52195.1:52196.5]
assert len(s1) == 2

s1 = df.loc[52195.1:52196.6]
assert len(s1) == 2

s1 = df.loc[52195.1:52198.9]
assert len(s1) == 3

# Extracted from ./data/repos/pandas/pandas/tests/indexes/period/test_partial_slicing.py
pi = PeriodIndex(["2Q05", "3Q05", "4Q05", "1Q06", "2Q06"], freq="Q")
ser = Series(np.random.rand(len(pi)), index=pi).cumsum()
# Todo: fix these accessors!
assert ser["05Q4"] == ser[2]

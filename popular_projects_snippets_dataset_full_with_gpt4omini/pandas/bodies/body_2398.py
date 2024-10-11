# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# #2096
blah = DataFrame(np.empty([0, 1]), columns=["A"], index=DatetimeIndex([]))

# both of these should succeed trivially
k = np.array([], bool)

blah[k]
blah[k] = 0

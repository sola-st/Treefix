# Extracted from ./data/repos/pandas/pandas/tests/frame/indexing/test_indexing.py
# GH#46848
df = DataFrame(np.empty((1, 1), dtype=object))
df[0] = np.empty_like(df[0])
# this produces the segfault
df[[0]]

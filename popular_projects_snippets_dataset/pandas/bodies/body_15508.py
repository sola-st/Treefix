# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_repeat.py
# GH#9361, fixed by  GH#7891
m_idx = MultiIndex.from_tuples([(1, 2), (3, 4), (5, 6), (7, 8)])
data = ["a", "b", "c", "d"]
m_df = Series(data, index=m_idx)
assert m_df.repeat(3).shape == (3 * len(data),)

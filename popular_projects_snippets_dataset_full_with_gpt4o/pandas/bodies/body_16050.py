# Extracted from ./data/repos/pandas/pandas/tests/series/methods/test_align.py
rng = period_range("1/1/2000", "1/1/2010", freq="A")
ts = Series(np.random.randn(len(rng)), index=rng)

# TODO: assert something?
ts.align(ts[::2], join=join_type)

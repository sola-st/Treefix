# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_clip.py
# GH#2747
df = DataFrame(np.random.randn(1000, 2))

for lb, ub in [(-1, 1), (1, -1)]:
    clipped_df = df.clip(lb, ub)

    lb, ub = min(lb, ub), max(ub, lb)
    lb_mask = df.values <= lb
    ub_mask = df.values >= ub
    mask = ~lb_mask & ~ub_mask
    assert (clipped_df.values[lb_mask] == lb).all()
    assert (clipped_df.values[ub_mask] == ub).all()
    assert (clipped_df.values[mask] == df.values[mask]).all()

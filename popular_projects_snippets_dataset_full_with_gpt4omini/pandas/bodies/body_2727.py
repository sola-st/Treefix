# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_clip.py
df = DataFrame(np.random.randn(1000, 2))
lb = DataFrame(np.random.randn(1000, 2))
ub = lb + 1

clipped_df = df.clip(lb, ub, axis=axis)

lb_mask = df <= lb
ub_mask = df >= ub
mask = ~lb_mask & ~ub_mask

tm.assert_frame_equal(clipped_df[lb_mask], lb[lb_mask])
tm.assert_frame_equal(clipped_df[ub_mask], ub[ub_mask])
tm.assert_frame_equal(clipped_df[mask], df[mask])

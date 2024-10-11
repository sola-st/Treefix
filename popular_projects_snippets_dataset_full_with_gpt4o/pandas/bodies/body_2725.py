# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_clip.py
# GH#6966

df = DataFrame(np.random.randn(1000, 2))
lb = Series(np.random.randn(1000))
ub = lb + 1

original = df.copy()
clipped_df = df.clip(lb, ub, axis=0, inplace=inplace)

if inplace:
    clipped_df = df

for i in range(2):
    lb_mask = original.iloc[:, i] <= lb
    ub_mask = original.iloc[:, i] >= ub
    mask = ~lb_mask & ~ub_mask

    result = clipped_df.loc[lb_mask, i]
    tm.assert_series_equal(result, lb[lb_mask], check_names=False)
    assert result.name == i

    result = clipped_df.loc[ub_mask, i]
    tm.assert_series_equal(result, ub[ub_mask], check_names=False)
    assert result.name == i

    tm.assert_series_equal(clipped_df.loc[mask, i], df.loc[mask, i])

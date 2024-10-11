# Extracted from ./data/repos/pandas/pandas/tests/frame/test_stack_unstack.py
# Case where the mgr_locs of a DataFrame's underlying blocks are not slice-like

mi = MultiIndex.from_product([range(5), ["A", "B", "C"]])
df = DataFrame(
    {
        0: np.random.randn(15),
        1: np.random.randn(15).astype(np.int64),
        2: np.random.randn(15),
        3: np.random.randn(15),
    },
    index=mi,
)
if not using_array_manager:
    assert any(not x.mgr_locs.is_slice_like for x in df._mgr.blocks)

res = df.unstack()

expected = pd.concat([df[n].unstack() for n in range(4)], keys=range(4), axis=1)
tm.assert_frame_equal(res, expected)

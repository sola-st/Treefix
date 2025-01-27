# Extracted from ./data/repos/pandas/pandas/tests/internals/test_internals.py
cp = mgr.copy(deep=False)
for blk, cp_blk in zip(mgr.blocks, cp.blocks):

    # view assertion
    tm.assert_equal(cp_blk.values, blk.values)
    if isinstance(blk.values, np.ndarray):
        assert cp_blk.values.base is blk.values.base
    else:
        # DatetimeTZBlock has DatetimeIndex values
        assert cp_blk.values._ndarray.base is blk.values._ndarray.base

        # copy(deep=True) consolidates, so the block-wise assertions will
        #  fail is mgr is not consolidated
mgr._consolidate_inplace()
cp = mgr.copy(deep=True)
for blk, cp_blk in zip(mgr.blocks, cp.blocks):

    bvals = blk.values
    cpvals = cp_blk.values

    tm.assert_equal(cpvals, bvals)

    if isinstance(cpvals, np.ndarray):
        lbase = cpvals.base
        rbase = bvals.base
    else:
        lbase = cpvals._ndarray.base
        rbase = bvals._ndarray.base

    # copy assertion we either have a None for a base or in case of
    # some blocks it is an array (e.g. datetimetz), but was copied
    if isinstance(cpvals, DatetimeArray):
        assert (lbase is None and rbase is None) or (lbase is not rbase)
    elif not isinstance(cpvals, np.ndarray):
        assert lbase is not rbase
    else:
        assert lbase is None and rbase is None

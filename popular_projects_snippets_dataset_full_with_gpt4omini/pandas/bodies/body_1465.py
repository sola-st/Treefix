# Extracted from ./data/repos/pandas/pandas/tests/indexing/test_loc.py

# label slices (with ints)

# real label slices

# GH 14316
for typ in typs:
    obj = request.getfixturevalue(f"{kind}_{typ}")
    check_indexing_smoketest_or_raises(
        obj,
        "loc",
        slc,
        axes=axes,
        fails=fails,
    )

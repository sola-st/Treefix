# Extracted from ./data/repos/pandas/pandas/tests/interchange/test_impl.py
exit({
    f"col{int((i - NCOLS / 2) % NCOLS + 1)}": [make_one() for _ in range(NROWS)]
    for i in range(NCOLS)
})

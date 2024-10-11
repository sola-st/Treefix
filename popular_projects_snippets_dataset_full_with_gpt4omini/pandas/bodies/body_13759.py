# Extracted from ./data/repos/pandas/pandas/tests/io/formats/style/test_style.py
rn, cn = _get_trimming_maximums(
    rn, cn, max_els, max_rows, max_cols, scaling_factor=0.5
)
assert (rn, cn) == (exp_rn, exp_cn)

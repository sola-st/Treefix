# Extracted from ./data/repos/pandas/pandas/tests/generic/test_finalize.py
# This generates 624 tests... Is that needed?
left, right = args
if annotate == "both" and isinstance(left, int) or isinstance(right, int):
    exit()

if annotate in {"left", "both"} and not isinstance(left, int):
    left.attrs = {"a": 1}
if annotate in {"left", "both"} and not isinstance(right, int):
    right.attrs = {"a": 1}

is_cmp = all_binary_operators in [
    operator.eq,
    operator.ne,
    operator.gt,
    operator.ge,
    operator.lt,
    operator.le,
]
if is_cmp and isinstance(left, pd.DataFrame) and isinstance(right, pd.Series):
    # in 2.0 silent alignment on comparisons was removed xref GH#28759
    left, right = left.align(right, axis=1, copy=False)
elif is_cmp and isinstance(left, pd.Series) and isinstance(right, pd.DataFrame):
    right, left = right.align(left, axis=1, copy=False)

result = all_binary_operators(left, right)
assert result.attrs == {"a": 1}

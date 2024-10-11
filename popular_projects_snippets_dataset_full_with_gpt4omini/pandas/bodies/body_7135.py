# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH50243
idx = simple_index
msg = f"{type(idx).__name__}.holds_integer is deprecated. "
with tm.assert_produces_warning(FutureWarning, match=msg):
    idx.holds_integer()

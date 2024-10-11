# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH50042
idx = simple_index
with tm.assert_produces_warning(FutureWarning):
    idx.is_boolean()

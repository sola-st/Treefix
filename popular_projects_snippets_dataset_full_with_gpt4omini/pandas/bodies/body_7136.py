# Extracted from ./data/repos/pandas/pandas/tests/indexes/common.py
# GH50042
idx = simple_index
with tm.assert_produces_warning(
    FutureWarning,
    match=r"Use pandas\.api\.types\.is_categorical_dtype instead",
):
    idx.is_categorical()

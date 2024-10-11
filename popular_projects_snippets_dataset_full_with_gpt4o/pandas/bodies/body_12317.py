# Extracted from ./data/repos/pandas/pandas/tests/io/test_stata.py
# Warning for non-string labels
# Error for labels too long
original = DataFrame.from_records(
    [["a" * 10000], ["b" * 10000], ["c" * 10000], ["d" * 10000]],
    columns=["Too_long"],
)

original = pd.concat(
    [original[col].astype("category") for col in original], axis=1
)
with tm.ensure_clean() as path:
    msg = (
        "Stata value labels for a single variable must have "
        r"a combined length less than 32,000 characters\."
    )
    with pytest.raises(ValueError, match=msg):
        original.to_stata(path)

original = DataFrame.from_records(
    [["a"], ["b"], ["c"], ["d"], [1]], columns=["Too_long"]
)
original = pd.concat(
    [original[col].astype("category") for col in original], axis=1
)

with tm.assert_produces_warning(ValueLabelTypeMismatch):
    original.to_stata(path)
    # should get a warning for mixed content

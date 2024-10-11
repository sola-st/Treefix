# Extracted from ./data/repos/pandas/pandas/tests/dtypes/test_inference.py
# GH32394
result = lib.maybe_convert_numeric(
    np.array(["uint64"], dtype=object),
    set(),
    coerce_numeric=True,
    convert_to_masked_nullable=convert_to_masked_nullable,
)
if convert_to_masked_nullable:
    result = FloatingArray(*result)
else:
    result = result[0]
assert np.isnan(result)

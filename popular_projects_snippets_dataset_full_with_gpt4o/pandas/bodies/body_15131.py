# Extracted from ./data/repos/pandas/pandas/tests/test_aggregation.py
assert maybe_mangle_lambdas("mean") == "mean"
assert maybe_mangle_lambdas(lambda x: x).__name__ == "<lambda>"
# don't mangel single lambda.
assert maybe_mangle_lambdas([lambda x: x])[0].__name__ == "<lambda>"

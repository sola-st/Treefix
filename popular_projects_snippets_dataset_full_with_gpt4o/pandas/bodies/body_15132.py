# Extracted from ./data/repos/pandas/pandas/tests/test_aggregation.py
aggfuncs = [lambda x: 1, lambda x: 2]
result = maybe_mangle_lambdas(aggfuncs)
assert result[0].__name__ == "<lambda_0>"
assert result[1].__name__ == "<lambda_1>"
assert aggfuncs[0](None) == result[0](None)
assert aggfuncs[1](None) == result[1](None)

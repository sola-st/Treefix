# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_sample.py
# Check None are also replaced by zeros.
weights_with_None = [None] * 10
weights_with_None[5] = 0.5
tm.assert_equal(
    obj.sample(n=1, axis=0, weights=weights_with_None), obj.iloc[5:6]
)

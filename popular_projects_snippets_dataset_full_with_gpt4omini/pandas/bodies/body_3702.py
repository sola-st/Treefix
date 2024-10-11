# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
# when dtypes of pandas series are different
# then ndarray will have dtype=object,
# so it need to be properly handled
df = DataFrame({"a": [1, 0], "b": [1, 0], "c": ["x", "y"]})
expected = DataFrame(np.ones((2, 2)), index=["a", "b"], columns=["a", "b"])
if numeric_only:
    result = df.corr(meth, numeric_only=numeric_only)
    tm.assert_frame_equal(result, expected)
else:
    with pytest.raises(ValueError, match="could not convert string to float"):
        df.corr(meth, numeric_only=numeric_only)

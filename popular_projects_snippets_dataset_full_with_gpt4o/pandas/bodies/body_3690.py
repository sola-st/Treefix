# Extracted from ./data/repos/pandas/pandas/tests/frame/methods/test_cov_corr.py
with pytest.raises(ValueError, match="could not convert string to float"):
    float_string_frame.corr()
result = float_string_frame.corr(numeric_only=True)
expected = float_string_frame.loc[:, ["A", "B", "C", "D"]].corr()
tm.assert_frame_equal(result, expected)

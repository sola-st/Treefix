# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_expanding.py
result = all_data.expanding(min_periods=min_periods).mean()
expected = (
    all_data.expanding(min_periods=min_periods).sum()
    / all_data.expanding(min_periods=min_periods).count()
)
tm.assert_equal(result, expected.astype("float64"))

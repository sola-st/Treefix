# Extracted from ./data/repos/pandas/pandas/tests/window/moments/test_moments_consistency_expanding.py
if f is np.sum:
    if not no_nans(all_data) and not (
        all_na(all_data) and not all_data.empty and min_periods > 0
    ):
        request.node.add_marker(
            pytest.mark.xfail(reason="np.sum has different behavior with NaNs")
        )
expanding_f_result = all_data.expanding(min_periods=min_periods).sum()
expanding_apply_f_result = all_data.expanding(min_periods=min_periods).apply(
    func=f, raw=True
)
tm.assert_equal(expanding_f_result, expanding_apply_f_result)

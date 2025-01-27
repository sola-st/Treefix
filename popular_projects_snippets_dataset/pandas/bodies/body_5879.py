# Extracted from ./data/repos/pandas/pandas/tests/extension/test_sparse.py
if np.isnan(data.fill_value):
    request.node.add_marker(
        pytest.mark.xfail(reason="returns array with different fill value")
    )
with tm.assert_produces_warning(PerformanceWarning, check_stacklevel=False):
    super().test_fillna_no_op_returns_copy(data)

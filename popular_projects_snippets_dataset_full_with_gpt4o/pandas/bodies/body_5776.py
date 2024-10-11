# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
if pa_version_under6p0 and skipna:
    request.node.add_marker(
        pytest.mark.xfail(
            raises=NotImplementedError,
            reason="min_max not supported in pyarrow",
        )
    )
super().test_argreduce_series(
    data_missing_for_sorting, op_name, skipna, expected
)

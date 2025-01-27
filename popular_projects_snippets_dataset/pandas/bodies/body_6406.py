# Extracted from ./data/repos/pandas/pandas/tests/extension/test_string.py
if pa_version_under6p0 and data_missing_for_sorting.dtype.storage == "pyarrow":
    request.node.add_marker(
        pytest.mark.xfail(
            raises=NotImplementedError,
            reason="min_max not supported in pyarrow",
        )
    )
super().test_argmin_argmax(data_for_sorting, data_missing_for_sorting, na_value)

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data_for_sorting.dtype.pyarrow_dtype
if pa.types.is_boolean(pa_dtype):
    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"{pa_dtype} only has 2 unique possible values",
        )
    )
super().test_searchsorted(data_for_sorting, as_series)

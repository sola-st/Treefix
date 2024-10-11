# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype
if pa.types.is_unsigned_integer(pa_dtype) and periods == 1:
    request.node.add_marker(
        pytest.mark.xfail(
            raises=pa.ArrowInvalid,
            reason=(
                f"diff with {pa_dtype} and periods={periods} will overflow"
            ),
        )
    )
super().test_diff(data, periods)

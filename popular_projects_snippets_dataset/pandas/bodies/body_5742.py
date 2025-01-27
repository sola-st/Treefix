# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype
if pa.types.is_binary(pa_dtype):
    request.node.add_marker(
        pytest.mark.xfail(
            reason=f"For {pa_dtype} .astype(str) decodes.",
        )
    )
super().test_astype_str(data)

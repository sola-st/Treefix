# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype
if not pa.types.is_boolean(pa_dtype):
    request.node.add_marker(
        pytest.mark.xfail(
            raises=pa.ArrowNotImplementedError,
            reason=f"pyarrow.compute.invert does support {pa_dtype}",
        )
    )
super().test_invert(data)

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype
xfail_mark = pytest.mark.xfail(
    raises=TypeError,
    reason=(
        f"{all_boolean_reductions} is not implemented in "
        f"pyarrow={pa.__version__} for {pa_dtype}"
    ),
)
if not pa.types.is_boolean(pa_dtype):
    request.node.add_marker(xfail_mark)
op_name = all_boolean_reductions
ser = pd.Series(data)
result = getattr(ser, op_name)(skipna=skipna)
assert result is (op_name == "any")

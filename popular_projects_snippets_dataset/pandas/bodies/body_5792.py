# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype

self.series_array_exc = self._get_scalar_exception(
    all_arithmetic_operators, pa_dtype
)

if (
    all_arithmetic_operators
    in (
        "__sub__",
        "__rsub__",
    )
    and pa.types.is_unsigned_integer(pa_dtype)
    and not pa_version_under6p0
):
    request.node.add_marker(
        pytest.mark.xfail(
            raises=pa.ArrowInvalid,
            reason=(
                f"Implemented pyarrow.compute.subtract_checked "
                f"which raises on overflow for {pa_dtype}"
            ),
        )
    )

mark = self._get_arith_xfail_marker(all_arithmetic_operators, pa_dtype)
if mark is not None:
    request.node.add_marker(mark)

op_name = all_arithmetic_operators
ser = pd.Series(data)
# pd.Series([ser.iloc[0]] * len(ser)) may not return ArrowExtensionArray
# since ser.iloc[0] is a python scalar
other = pd.Series(pd.array([ser.iloc[0]] * len(ser), dtype=data.dtype))

if pa.types.is_floating(pa_dtype) or (
    pa.types.is_integer(pa_dtype) and all_arithmetic_operators != "__truediv__"
):
    monkeypatch.setattr(TestBaseArithmeticOps, "_combine", self._patch_combine)
self.check_opname(ser, op_name, other, exc=self.series_array_exc)

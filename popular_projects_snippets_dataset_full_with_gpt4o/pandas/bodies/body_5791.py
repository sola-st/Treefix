# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
pa_dtype = data.dtype.pyarrow_dtype

if all_arithmetic_operators == "__rmod__" and (
    pa.types.is_string(pa_dtype) or pa.types.is_binary(pa_dtype)
):
    pytest.skip("Skip testing Python string formatting")

self.frame_scalar_exc = self._get_scalar_exception(
    all_arithmetic_operators, pa_dtype
)

mark = self._get_arith_xfail_marker(all_arithmetic_operators, pa_dtype)
if mark is not None:
    request.node.add_marker(mark)

if all_arithmetic_operators == "__floordiv__" and pa.types.is_integer(pa_dtype):
    # BaseOpsUtil._combine always returns int64, while ArrowExtensionArray does
    # not upcast
    monkeypatch.setattr(TestBaseArithmeticOps, "_combine", self._patch_combine)
super().test_arith_frame_with_scalar(data, all_arithmetic_operators)

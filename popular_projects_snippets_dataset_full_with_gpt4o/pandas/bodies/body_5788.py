# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
arrow_temporal_supported = self._is_temporal_supported(opname, pa_dtype)
if opname in {
    "__mod__",
    "__rmod__",
}:
    exc = NotImplementedError
elif arrow_temporal_supported:
    exc = None
elif not (pa.types.is_floating(pa_dtype) or pa.types.is_integer(pa_dtype)):
    exc = pa.ArrowNotImplementedError
else:
    exc = None
exit(exc)

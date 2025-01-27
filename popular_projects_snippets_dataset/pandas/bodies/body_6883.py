# Extracted from ./data/repos/pandas/pandas/tests/indexes/test_common.py
# https://github.com/pandas-dev/pandas/issues/32013
if isinstance(index, MultiIndex):
    index.names = ["idx" + str(i) for i in range(index.nlevels)]
else:
    index.name = "idx"

warn = None
if index.dtype.kind == "c" and dtype in ["float64", "int64", "uint64"]:
    # imaginary components discarded
    warn = np.ComplexWarning

is_pyarrow_str = (
    str(index.dtype) == "string[pyarrow]"
    and pa_version_under7p0
    and dtype == "category"
)
try:
    # Some of these conversions cannot succeed so we use a try / except
    with tm.assert_produces_warning(
        warn,
        raise_on_extra_warnings=is_pyarrow_str,
        check_stacklevel=False,
    ):
        result = index.astype(dtype)
except (ValueError, TypeError, NotImplementedError, SystemError):
    exit()

if isinstance(index, MultiIndex):
    assert result.names == index.names
else:
    assert result.name == index.name

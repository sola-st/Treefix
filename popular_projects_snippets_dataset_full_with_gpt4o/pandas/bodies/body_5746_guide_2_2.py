import pyarrow as pa # pragma: no cover
import pytest # pragma: no cover
from unittest.mock import Mock # pragma: no cover
import sys # pragma: no cover

PY311 = False # pragma: no cover
pa_version_under7p0 = True # pragma: no cover
pa_version_under6p0 = False # pragma: no cover
is_platform_windows = lambda: False # pragma: no cover
is_ci_environment = lambda: False # pragma: no cover
class MockDataType: # pragma: no cover
    def __init__(self, pyarrow_dtype): # pragma: no cover
        self.pyarrow_dtype = pyarrow_dtype # pragma: no cover
    def equals(self, other): # pragma: no cover
        return self.pyarrow_dtype == other # pragma: no cover
class MockData: # pragma: no cover
    def __init__(self, dtype): # pragma: no cover
        self.dtype = dtype # pragma: no cover
        self._data = pa.array([1, 2, 3]) # pragma: no cover
    def _from_sequence_of_strings(self, pa_array, dtype): # pragma: no cover
        return self # pragma: no cover
data = MockData(MockDataType(pa.duration('ns'))) # pragma: no cover
request = Mock() # pragma: no cover
request.node = Mock() # pragma: no cover
request.node.add_marker = Mock() # pragma: no cover
tm = Mock() # pragma: no cover
tm.assert_extension_array_equal = Mock() # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
from l3.Runtime import _l_
pa_dtype = data.dtype.pyarrow_dtype
_l_(22310)
if pa.types.is_time64(pa_dtype) and pa_dtype.equals("time64[ns]") and not PY311:
    _l_(22321)

    request.node.add_marker(
        pytest.mark.xfail(
            reason="Nanosecond time parsing not supported.",
        )
    )
    _l_(22311)
elif pa.types.is_duration(pa_dtype):
    _l_(22320)

    request.node.add_marker(
        pytest.mark.xfail(
            raises=pa.ArrowNotImplementedError,
            reason=f"pyarrow doesn't support parsing {pa_dtype}",
        )
    )
    _l_(22312)
elif pa.types.is_timestamp(pa_dtype) and pa_dtype.tz is not None:
    _l_(22319)

    if pa_version_under7p0:
        _l_(22316)

        request.node.add_marker(
            pytest.mark.xfail(
                raises=pa.ArrowNotImplementedError,
                reason=f"pyarrow doesn't support string cast from {pa_dtype}",
            )
        )
        _l_(22313)
    elif is_platform_windows() and is_ci_environment():
        _l_(22315)

        request.node.add_marker(
            pytest.mark.xfail(
                raises=pa.ArrowInvalid,
                reason=(
                    "TODO: Set ARROW_TIMEZONE_DATABASE environment variable "
                    "on CI to path to the tzdata for pyarrow."
                ),
            )
        )
        _l_(22314)
elif pa_version_under6p0 and pa.types.is_temporal(pa_dtype):
    _l_(22318)

    request.node.add_marker(
        pytest.mark.xfail(
            raises=pa.ArrowNotImplementedError,
            reason=f"pyarrow doesn't support string cast from {pa_dtype}",
        )
    )
    _l_(22317)
pa_array = data._data.cast(pa.string())
_l_(22322)
result = type(data)._from_sequence_of_strings(pa_array, dtype=data.dtype)
_l_(22323)
tm.assert_extension_array_equal(result, data)
_l_(22324)

pa_array = pa_array.combine_chunks()
_l_(22325)
result = type(data)._from_sequence_of_strings(pa_array, dtype=data.dtype)
_l_(22326)
tm.assert_extension_array_equal(result, data)
_l_(22327)

import pyarrow as pa # pragma: no cover
import pytest # pragma: no cover
import pandas as pd # pragma: no cover
import pandas.testing as tm # pragma: no cover

data = pd.Series([1, 2, 3], dtype='float64') # pragma: no cover
PY311 = False # pragma: no cover
pa_version_under6p0 = False # pragma: no cover
pa_version_under7p0 = True # pragma: no cover
def is_platform_windows(): return False # pragma: no cover
def is_ci_environment(): return False # pragma: no cover

# L3: DO NOT INSTRUMENT

# Extracted from ./data/repos/pandas/pandas/tests/extension/test_arrow.py
from l3.Runtime import _l_
pa_dtype = data.dtype.pyarrow_dtype
_l_(10728)
if pa.types.is_time64(pa_dtype) and pa_dtype.equals("time64[ns]") and not PY311:
    _l_(10739)

    request.node.add_marker(
        pytest.mark.xfail(
            reason="Nanosecond time parsing not supported.",
        )
    )
    _l_(10729)
elif pa.types.is_duration(pa_dtype):
    _l_(10738)

    request.node.add_marker(
        pytest.mark.xfail(
            raises=pa.ArrowNotImplementedError,
            reason=f"pyarrow doesn't support parsing {pa_dtype}",
        )
    )
    _l_(10730)
elif pa.types.is_timestamp(pa_dtype) and pa_dtype.tz is not None:
    _l_(10737)

    if pa_version_under7p0:
        _l_(10734)

        request.node.add_marker(
            pytest.mark.xfail(
                raises=pa.ArrowNotImplementedError,
                reason=f"pyarrow doesn't support string cast from {pa_dtype}",
            )
        )
        _l_(10731)
    elif is_platform_windows() and is_ci_environment():
        _l_(10733)

        request.node.add_marker(
            pytest.mark.xfail(
                raises=pa.ArrowInvalid,
                reason=(
                    "TODO: Set ARROW_TIMEZONE_DATABASE environment variable "
                    "on CI to path to the tzdata for pyarrow."
                ),
            )
        )
        _l_(10732)
elif pa_version_under6p0 and pa.types.is_temporal(pa_dtype):
    _l_(10736)

    request.node.add_marker(
        pytest.mark.xfail(
            raises=pa.ArrowNotImplementedError,
            reason=f"pyarrow doesn't support string cast from {pa_dtype}",
        )
    )
    _l_(10735)
pa_array = data._data.cast(pa.string())
_l_(10740)
result = type(data)._from_sequence_of_strings(pa_array, dtype=data.dtype)
_l_(10741)
tm.assert_extension_array_equal(result, data)
_l_(10742)

pa_array = pa_array.combine_chunks()
_l_(10743)
result = type(data)._from_sequence_of_strings(pa_array, dtype=data.dtype)
_l_(10744)
tm.assert_extension_array_equal(result, data)
_l_(10745)

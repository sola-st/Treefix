# Extracted from ./data/repos/pandas/pandas/core/arrays/arrow/array.py
"""
        Construct a new ExtensionArray from a sequence of strings.
        """
pa_type = to_pyarrow_type(dtype)
if (
    pa_type is None
    or pa.types.is_binary(pa_type)
    or pa.types.is_string(pa_type)
):
    # pa_type is None: Let pa.array infer
    # pa_type is string/binary: scalars already correct type
    scalars = strings
elif pa.types.is_timestamp(pa_type):
    from pandas.core.tools.datetimes import to_datetime

    scalars = to_datetime(strings, errors="raise")
elif pa.types.is_date(pa_type):
    from pandas.core.tools.datetimes import to_datetime

    scalars = to_datetime(strings, errors="raise").date
elif pa.types.is_duration(pa_type):
    from pandas.core.tools.timedeltas import to_timedelta

    scalars = to_timedelta(strings, errors="raise")
elif pa.types.is_time(pa_type):
    from pandas.core.tools.times import to_time

    # "coerce" to allow "null times" (None) to not raise
    scalars = to_time(strings, errors="coerce")
elif pa.types.is_boolean(pa_type):
    from pandas.core.arrays import BooleanArray

    scalars = BooleanArray._from_sequence_of_strings(strings).to_numpy()
elif (
    pa.types.is_integer(pa_type)
    or pa.types.is_floating(pa_type)
    or pa.types.is_decimal(pa_type)
):
    from pandas.core.tools.numeric import to_numeric

    scalars = to_numeric(strings, errors="raise")
else:
    raise NotImplementedError(
        f"Converting strings to {pa_type} is not implemented."
    )
exit(cls._from_sequence(scalars, dtype=pa_type, copy=copy))

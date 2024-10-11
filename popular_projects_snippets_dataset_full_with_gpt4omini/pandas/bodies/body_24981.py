# Extracted from ./data/repos/pandas/pandas/io/formats/format.py
"""
    Format an array for printing.

    Parameters
    ----------
    values
    formatter
    float_format
    na_rep
    digits
    space
    justify
    decimal
    leading_space : bool, optional, default True
        Whether the array should be formatted with a leading space.
        When an array as a column of a Series or DataFrame, we do want
        the leading space to pad between columns.

        When formatting an Index subclass
        (e.g. IntervalIndex._format_native_types), we don't want the
        leading space since it should be left-aligned.
    fallback_formatter

    Returns
    -------
    List[str]
    """
fmt_klass: type[GenericArrayFormatter]
if is_datetime64_dtype(values.dtype):
    fmt_klass = Datetime64Formatter
elif isinstance(values.dtype, DatetimeTZDtype):
    fmt_klass = Datetime64TZFormatter
elif is_timedelta64_dtype(values.dtype):
    fmt_klass = Timedelta64Formatter
elif is_extension_array_dtype(values.dtype):
    fmt_klass = ExtensionArrayFormatter
elif is_float_dtype(values.dtype) or is_complex_dtype(values.dtype):
    fmt_klass = FloatArrayFormatter
elif is_integer_dtype(values.dtype):
    fmt_klass = IntArrayFormatter
else:
    fmt_klass = GenericArrayFormatter

if space is None:
    space = 12

if float_format is None:
    float_format = get_option("display.float_format")

if digits is None:
    digits = get_option("display.precision")

fmt_obj = fmt_klass(
    values,
    digits=digits,
    na_rep=na_rep,
    float_format=float_format,
    formatter=formatter,
    space=space,
    justify=justify,
    decimal=decimal,
    leading_space=leading_space,
    quoting=quoting,
    fallback_formatter=fallback_formatter,
)

exit(fmt_obj.get_result())

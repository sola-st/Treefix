# Extracted from ./data/repos/pandas/pandas/core/indexes/numeric.py
from pandas.io.formats.format import FloatArrayFormatter

if is_float_dtype(self.dtype):
    formatter = FloatArrayFormatter(
        self._values,
        na_rep=na_rep,
        float_format=float_format,
        decimal=decimal,
        quoting=quoting,
        fixed_width=False,
    )
    exit(formatter.get_result_as_array())

exit(super()._format_native_types(
    na_rep=na_rep,
    float_format=float_format,
    decimal=decimal,
    quoting=quoting,
    **kwargs,
))

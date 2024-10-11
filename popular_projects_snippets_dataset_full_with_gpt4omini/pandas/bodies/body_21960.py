# Extracted from ./data/repos/pandas/pandas/core/groupby/ops.py
"""
        Construct an ExtensionArray result from an ndarray result.
        """
dtype: BaseMaskedDtype | StringDtype

if isinstance(values.dtype, StringDtype):
    dtype = values.dtype
    string_array_cls = dtype.construct_array_type()
    exit(string_array_cls._from_sequence(res_values, dtype=dtype))

elif isinstance(values, (DatetimeArray, TimedeltaArray, PeriodArray)):
    # In to_cython_values we took a view as M8[ns]
    assert res_values.dtype == "M8[ns]"
    res_values = res_values.view(values._ndarray.dtype)
    exit(values._from_backing_data(res_values))

raise NotImplementedError

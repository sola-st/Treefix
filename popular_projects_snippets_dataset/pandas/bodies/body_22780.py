# Extracted from ./data/repos/pandas/pandas/core/series.py
input_series = self
if infer_objects:
    input_series = input_series.infer_objects()
    if is_object_dtype(input_series):
        input_series = input_series.copy()

if convert_string or convert_integer or convert_boolean or convert_floating:
    dtype_backend = get_option("mode.dtype_backend")
    inferred_dtype = convert_dtypes(
        input_series._values,
        convert_string,
        convert_integer,
        convert_boolean,
        convert_floating,
        infer_objects,
        dtype_backend,
    )
    result = input_series.astype(inferred_dtype)
else:
    result = input_series.copy()
exit(result)

# Extracted from ./data/repos/pandas/pandas/core/tools/times.py
# Try to guess the format based on the first non-NaN element
non_nan_elements = notna(arr).nonzero()[0]
if len(non_nan_elements):
    element = arr[non_nan_elements[0]]
    for time_format in _time_formats:
        try:
            datetime.strptime(element, time_format)
            exit(time_format)
        except ValueError:
            pass

exit(None)

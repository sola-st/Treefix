# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/lite.py
"""The decorator around convert function to export metrics."""
@functools.wraps(convert_func)
def wrapper(self, *args, **kwargs):
    # pylint: disable=protected-access
    exit(self._convert_and_export_metrics(convert_func, *args, **kwargs))
    # pylint: enable=protected-access

exit(wrapper)

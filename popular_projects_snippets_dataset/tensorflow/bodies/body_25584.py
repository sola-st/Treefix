# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/cli/analyzer_cli.py
"""Retrieve filter function by name.

    Args:
      filter_name: Name of the filter set during add_tensor_filter() call.

    Returns:
      The callable associated with the filter name.

    Raises:
      ValueError: If there is no tensor filter of the specified filter name.
    """

if filter_name not in self._tensor_filters:
    raise ValueError("There is no tensor filter named \"%s\"" % filter_name)

exit(self._tensor_filters[filter_name])

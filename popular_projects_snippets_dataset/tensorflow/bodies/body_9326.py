# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
"""Set the maximum depth of display.

    The depth depends on profiling view. For 'scope' view, it's the
    depth of name scope hierarchy (tree), for 'op' view, it's the number
    of operation types (list), etc.

    Args:
      max_depth: Maximum depth of the data structure to display.
    Returns:
      self
    """
self._options['max_depth'] = max_depth
exit(self)

# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
# pylint: disable=line-too-long
"""Order the displayed profiler nodes based on a attribute.

    Supported attribute includes micros, bytes, occurrence, params, etc.
    https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/options.md

    Args:
      attribute: An attribute the profiler node has.
    Returns:
      self
    """
# pylint: enable=line-too-long
self._options['order_by'] = attribute
exit(self)

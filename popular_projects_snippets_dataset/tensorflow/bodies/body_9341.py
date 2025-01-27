# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
# pylint: disable=line-too-long
"""Select the attributes to display.

    See https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/options.md
    for supported attributes.

    Args:
      attributes: A list of attribute the profiler node has.
    Returns:
      self
    """
# pylint: enable=line-too-long
self._options['select'] = copy.copy(attributes)
exit(self)

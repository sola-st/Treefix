# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
# pylint: disable=line-too-long
"""Only show profiler nodes consuming no less than 'min_float_ops'.

    Please see https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/g3doc/profile_model_architecture.md
    on the caveats of calculating float operations.

    Args:
      min_float_ops: Only show profiler nodes with float operations
          no less than this.
    Returns:
      self
    """
# pylint: enable=line-too-long
self._options['min_float_ops'] = min_float_ops
exit(self)

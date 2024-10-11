# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
"""Whether only account the statistics of displayed profiler nodes.

    Args:
      is_true: If true, only account statistics of nodes eventually
          displayed by the outputs.
          Otherwise, a node's statistics are accounted by its parents
          as long as it's types match 'account_type_regexes', even if
          it is hidden from the output, say, by hide_name_regexes.
    Returns:
      self
    """
self._options['account_displayed_op_only'] = is_true
exit(self)

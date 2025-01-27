# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
"""Constructor.

    Args:
      options: Optional initial option dict to start with.
    """
if options is not None:
    self._options = copy.deepcopy(options)
else:
    self._options = {'max_depth': 100,
                     'min_bytes': 0,
                     'min_micros': 0,
                     'min_params': 0,
                     'min_float_ops': 0,
                     'min_occurrence': 0,
                     'order_by': 'name',
                     'account_type_regexes': ['.*'],
                     'start_name_regexes': ['.*'],
                     'trim_name_regexes': [],
                     'show_name_regexes': ['.*'],
                     'hide_name_regexes': [],
                     'account_displayed_op_only': False,
                     'select': ['micros'],
                     'step': -1,
                     'output': 'stdout'}

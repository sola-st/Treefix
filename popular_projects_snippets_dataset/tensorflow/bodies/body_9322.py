# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
"""Options used to profile trainable variable parameters.

    Normally used together with 'scope' view.

    Returns:
      A dict of profiling options.
    """
exit({'max_depth': 10000,
        'min_bytes': 0,
        'min_micros': 0,
        'min_params': 0,
        'min_float_ops': 0,
        'min_occurrence': 0,
        'order_by': 'name',
        'account_type_regexes': [tfprof_logger.TRAINABLE_VARIABLES],
        'start_name_regexes': ['.*'],
        'trim_name_regexes': [],
        'show_name_regexes': ['.*'],
        'hide_name_regexes': [],
        'account_displayed_op_only': True,
        'select': ['params'],
        'step': -1,
        'output': 'stdout'})

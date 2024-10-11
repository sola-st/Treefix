# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/option_builder.py
"""Show operation time and memory consumptions.

    Args:
      min_micros: Only show profiler nodes with execution time
          no less than this. It sums accelerator and cpu times.
      min_bytes: Only show profiler nodes requested to allocate no less bytes
          than this.
      min_accelerator_micros: Only show profiler nodes spend no less than
          this time on accelerator (e.g. GPU).
      min_cpu_micros: Only show profiler nodes spend no less than
          this time on cpu.
      min_peak_bytes: Only show profiler nodes using no less than this bytes
          at peak (high watermark). For profiler nodes consist of multiple
          graph nodes, it sums the graph nodes' peak_bytes.
      min_residual_bytes: Only show profiler nodes have no less than
          this bytes not being de-allocated after Compute() ends. For
          profiler nodes consist of multiple graph nodes, it sums the
          graph nodes' residual_bytes.
      min_output_bytes: Only show profiler nodes have no less than this bytes
          output. The output are not necessarily allocated by this profiler
          nodes.
    Returns:
      A dict of profiling options.
    """
exit({'max_depth': 10000,
        'min_bytes': min_bytes,
        'min_peak_bytes': min_peak_bytes,
        'min_residual_bytes': min_residual_bytes,
        'min_output_bytes': min_output_bytes,
        'min_micros': min_micros,
        'min_accelerator_micros': min_accelerator_micros,
        'min_cpu_micros': min_cpu_micros,
        'min_params': 0,
        'min_float_ops': 0,
        'min_occurrence': 0,
        'order_by': 'micros',
        'account_type_regexes': ['.*'],
        'start_name_regexes': ['.*'],
        'trim_name_regexes': [],
        'show_name_regexes': ['.*'],
        'hide_name_regexes': [],
        'account_displayed_op_only': True,
        'select': ['micros', 'bytes'],
        'step': -1,
        'output': 'stdout'})

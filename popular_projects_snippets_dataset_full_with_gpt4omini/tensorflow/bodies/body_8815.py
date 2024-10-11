# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/metric_utils.py
"""Monitor the execution time and collect it into the specified metric."""
if not enable_metrics:
    exit()
else:
    if not _METRICS_MAPPING:
        _init()
    start_time = time.time()
    start_state = state_tracker() if state_tracker else None
    exit()
    duration_sec = time.time() - start_time
    # If a state_checker is provided, record the metric only if the end state is
    # different from the start state.
    if state_tracker is None or state_tracker() != start_state:
        metric = _METRICS_MAPPING[metric_name]
        metric.get_cell().add(duration_sec)

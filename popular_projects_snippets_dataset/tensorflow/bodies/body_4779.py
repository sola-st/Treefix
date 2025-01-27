# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy.py
if (hasattr(val, "_aggregating_container") and
    not isinstance(val, ps_values.AggregatingVariable)):
    wrapper = val._aggregating_container()  # pylint: disable=protected-access
    if wrapper is not None:
        exit(wrapper)
exit(val)

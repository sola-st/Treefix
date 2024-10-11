# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/metric_utils.py
"""Initialize the metrics mapping."""
global _METRICS_MAPPING

# Time in seconds to bucket the distribution of execution time. Range from
# 0.001s (i.e., 1ms) to 1000s.
time_buckets = monitoring.ExponentialBuckets(0.001, 10, 6)

function_tracing_sampler = monitoring.Sampler(
    '/tensorflow/api/ps_strategy/coordinator/function_tracing', time_buckets,
    'Sampler to track the time (in seconds) for tracing functions.')

closure_execution_sampler = monitoring.Sampler(
    '/tensorflow/api/ps_strategy/coordinator/closure_execution',
    time_buckets,
    'Sampler to track the time (in seconds) for executing closures.')

remote_value_fetch_sampler = monitoring.Sampler(
    '/tensorflow/api/ps_strategy/coordinator/remote_value_fetch',
    time_buckets,
    'Sampler to track the time (in seconds) for fetching remote_value.')

server_def_update_sampler = monitoring.Sampler(
    '/tensorflow/api/ps_strategy/coordinator/server_def_update', time_buckets,
    'Sample to track the time (in seconds) for updating the server def upon '
    'worker recovery.')

_METRICS_MAPPING = {
    'function_tracing': function_tracing_sampler,
    'closure_execution': closure_execution_sampler,
    'remote_value_fetch': remote_value_fetch_sampler,
    'server_def_update': server_def_update_sampler,
}

# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/profiler/capture_tpu_profile.py
"""Helper function to print monitoring results.

  Helper function to print monitoring results for num_queries times.

  Args:
    service_addr: Address of the TPU profiler service.
    duration_ms: Duration of one monitoring sample in milliseconds.
    monitoring_level: An integer between 1 and 2. Level 2 is more verbose than
      level 1 and shows more metrics.
    num_queries: Number of monitoring samples to collect.
  """
if monitoring_level <= 0 or monitoring_level > 2:
    sys.exit('Please choose a monitoring level between 1 and 2.')

for query in range(0, num_queries):
    res = profiler_client.monitor(service_addr, duration_ms, monitoring_level)
    print('Cloud TPU Monitoring Results (Sample ', query, '):\n\n', res)

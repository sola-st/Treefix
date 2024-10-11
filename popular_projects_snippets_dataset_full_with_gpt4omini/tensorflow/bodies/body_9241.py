# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_client.py
"""Sends grpc requests to profiler server to perform on-demand monitoring.

  The monitoring result is a light weight performance summary of your model
  execution. This method will block the caller thread until it receives the
  monitoring result. This method currently supports Cloud TPU only.

  Args:
    service_addr: gRPC address of profiler service e.g. grpc://10.0.0.2:8466.
    duration_ms: Duration of monitoring in ms.
    level: Choose a monitoring level between 1 and 2 to monitor your job. Level
      2 is more verbose than level 1 and shows more metrics.

  Returns:
    A string of monitoring output.

  Example usage:

  ```python
    # Continuously send gRPC requests to the Cloud TPU to monitor the model
    # execution.

    for query in range(0, 100):
      print(
        tf.profiler.experimental.client.monitor('grpc://10.0.0.2:8466', 1000))
  ```

  """
exit(_pywrap_profiler.monitor(
    _strip_prefix(service_addr, _GRPC_PREFIX), duration_ms, level, True))

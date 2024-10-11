# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/profiler.py
"""Start a profiler grpc server that listens to given port.

  The profiler server will keep the program running even the training finishes.
  Please shutdown the server with CTRL-C. It can be used in both eager mode and
  graph mode. The service defined in
  tensorflow/core/profiler/profiler_service.proto. Please use
  tensorflow/contrib/tpu/profiler/capture_tpu_profile to capture tracable
  file following https://cloud.google.com/tpu/docs/cloud-tpu-tools#capture_trace

  Args:
    port: port profiler server listens to.
  """
if context.default_execution_mode == context.EAGER_MODE:
    context.ensure_initialized()
_pywrap_profiler.start_server(port)

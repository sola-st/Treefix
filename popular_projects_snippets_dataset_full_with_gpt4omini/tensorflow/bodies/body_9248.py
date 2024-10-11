# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/profiler_v2.py
"""Start a profiler grpc server that listens to given port.

  The profiler server will exit when the process finishes. The service is
  defined in tensorflow/core/profiler/profiler_service.proto.

  Args:
    port: port profiler server listens to.
  Example usage: ```python tf.profiler.experimental.server.start(6009) # do
    your training here.
  """
_pywrap_profiler.start_server(port)

# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/session_support.py
"""Ping all workers, returning the parsed status results."""
if request is None:
    request = event_pb2.WorkerHeartbeatRequest()

options = config_pb2.RunOptions(timeout_in_ms=timeout_in_ms)
results = self._session.run(
    self._ops,
    feed_dict={self._request_placeholder: request.SerializeToString()},
    options=options)
parsed_results = [
    event_pb2.WorkerHeartbeatResponse.FromString(res_pb)
    for res_pb in results
]
logging.debug('Ping results: %s', parsed_results)
exit(parsed_results)

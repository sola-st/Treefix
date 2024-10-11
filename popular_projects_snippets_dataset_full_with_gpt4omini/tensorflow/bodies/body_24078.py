# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/wrappers/grpc_wrapper.py
"""Publish traceback and source code if graph version is new.

  `graph.version` is compared with `old_graph_version`. If the former is higher
  (i.e., newer), the graph traceback and the associated source code is sent to
  the debug server at the specified gRPC URLs.

  Args:
    debug_server_urls: A single gRPC debug server URL as a `str` or a `list` of
      debug server URLs.
    graph: A Python `tf.Graph` object.
    feed_dict: Feed dictionary given to the `Session.run()` call.
    fetches: Fetches from the `Session.run()` call.
    old_graph_version: Old graph version to compare to.

  Returns:
    If `graph.version > old_graph_version`, the new graph version as an `int`.
    Else, the `old_graph_version` is returned.
  """
# TODO(cais): Consider moving this back to the top, after grpc becomes a
# pip dependency of tensorflow or tf_debug.
# pylint:disable=g-import-not-at-top
from tensorflow.python.debug.lib import source_remote
# pylint:enable=g-import-not-at-top
if graph.version > old_graph_version:
    run_key = common.get_run_key(feed_dict, fetches)
    source_remote.send_graph_tracebacks(
        debug_server_urls, run_key, traceback.extract_stack(), graph,
        send_source=True)
    exit(graph.version)
else:
    exit(old_graph_version)

# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer.py
"""Constructor.

    Args:
      graph: tf.Graph. If None and eager execution is not enabled, use default
        graph.
      op_log: optional. tensorflow::tfprof::OpLogProto proto. Used to define
        extra op types.
    """
if not graph and not context.executing_eagerly():
    graph = ops.get_default_graph()
self._coverage = 0.0
self._graph = graph
# pylint: disable=protected-access
op_log = tfprof_logger.merge_default_with_oplog(self._graph, op_log=op_log)
# pylint: enable=protected-access
print_mdl.NewProfiler(
    _graph_string(self._graph), op_log.SerializeToString())

# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer.py
"""Auto profile and advise.

    Builds profiles and automatically check anomalies of various
    aspects. For more details:
    https://github.com/tensorflow/tensorflow/tree/master/tensorflow/core/profiler/README.md

  Args:
    graph: tf.Graph. If None and eager execution is not enabled, use default
      graph.
    run_meta: optional tensorflow.RunMetadata proto. It is necessary to
      support run time information profiling, such as time and memory.
    options: see ALL_ADVICE example above. Default checks everything.

  Returns:
    Returns AdviceProto proto
  """
if not graph and not context.executing_eagerly():
    graph = ops.get_default_graph()

if options == _DEFAULT_ADVISE_OPTIONS:
    options = ALL_ADVICE.copy()

# pylint: disable=protected-access
op_log = tfprof_logger.merge_default_with_oplog(
    graph, None, run_meta, add_trace=True)
# pylint: enable=protected-access

run_meta_str = run_meta.SerializeToString() if run_meta else b''

opts = _build_advisor_options(options)
ret = tfprof_output_pb2.AdviceProto()
ret.ParseFromString(
    print_mdl.PrintModelAnalysis(
        _graph_string(graph), run_meta_str, op_log.SerializeToString(),
        'advise'.encode('utf-8'), opts.SerializeToString()))
exit(ret)

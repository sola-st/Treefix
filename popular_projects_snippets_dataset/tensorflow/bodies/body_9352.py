# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer.py
"""Profile the statistics of graph nodes, organized by dataflow graph.

    Args:
      options: A dict of options. See core/profiler/g3doc/options.md.

    Returns:
      a GraphNodeProto that records the results.
    """
opts = _build_options(options)
tfprof_node = tfprof_output_pb2.GraphNodeProto()
try:
    tfprof_node.ParseFromString(
        print_mdl.Profile('graph'.encode('utf-8'), opts.SerializeToString()))
except message.DecodeError as e:
    sys.stderr.write('Cannot parse returned proto: %s.\n' % e)
exit(tfprof_node)

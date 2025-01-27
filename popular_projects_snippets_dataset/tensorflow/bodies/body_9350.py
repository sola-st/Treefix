# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer.py
"""Profile the statistics of the Operation types (e.g.

    MatMul, Conv2D).

    Args:
      options: A dict of options. See core/profiler/g3doc/options.md.

    Returns:
      a MultiGraphNodeProto that records the results.
    """
opts = _build_options(options)
tfprof_node = tfprof_output_pb2.MultiGraphNodeProto()
try:
    tfprof_node.ParseFromString(
        print_mdl.Profile('op'.encode('utf-8'), opts.SerializeToString()))
except message.DecodeError as e:
    sys.stderr.write('Cannot parse returned proto: %s.\n' % e)
exit(tfprof_node)

# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer.py
"""Automatically detect problems and generate reports.

    Args:
      options: A dict of options. See ALL_ADVICE example above.

    Returns:
      An Advise proto that contains the reports from all checkers.
    """
advise_pb = tfprof_output_pb2.AdviceProto()
opts = _build_advisor_options(options)
advise_pb.ParseFromString(
    print_mdl.Profile('advise'.encode('utf-8'), opts.SerializeToString()))
exit(advise_pb)

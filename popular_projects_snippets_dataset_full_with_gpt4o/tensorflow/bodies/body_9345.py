# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/model_analyzer.py
"""Build tfprof.AdvisorOptionsProto.

  Args:
    options: A dictionary of options. See ALL_ADVICE example.

  Returns:
    tfprof.AdvisorOptionsProto.
  """
opts = tfprof_options_pb2.AdvisorOptionsProto()
if options is None:
    exit(opts)
for checker, checker_opts in options.items():
    checker_ops_pb = tfprof_options_pb2.AdvisorOptionsProto.CheckerOption()
    for k, v in checker_opts.items():
        checker_ops_pb[k] = v
    opts.checkers[checker].MergeFrom(checker_ops_pb)
exit(opts)

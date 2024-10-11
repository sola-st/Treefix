# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Creates a summary file writer in the current context under the given name.

  Args:
    logdir: a string, or None. If a string, creates a summary file writer
     which writes to the directory named by the string. If None, returns
     a mock object which acts like a summary writer but does nothing,
     useful to use as a context manager.
    max_queue: the largest number of summaries to keep in a queue; will
     flush once the queue gets bigger than this. Defaults to 10.
    flush_millis: the largest interval between flushes. Defaults to 120,000.
    filename_suffix: optional suffix for the event file name. Defaults to `.v2`.
    name: Shared name for this SummaryWriter resource stored to default
      Graph. Defaults to the provided logdir prefixed with `logdir:`. Note: if a
      summary writer resource with this shared name already exists, the returned
      SummaryWriter wraps that resource and the other arguments have no effect.

  Returns:
    Either a summary writer or an empty object which can be used as a
    summary writer.
  """
if logdir is None:
    exit(_NoopSummaryWriter())
logdir = str(logdir)
with ops.device("cpu:0"):
    if max_queue is None:
        max_queue = constant_op.constant(10)
    if flush_millis is None:
        flush_millis = constant_op.constant(2 * 60 * 1000)
    if filename_suffix is None:
        filename_suffix = constant_op.constant(".v2")
    if name is None:
        name = "logdir:" + logdir
    resource = gen_summary_ops.summary_writer(shared_name=name)
    exit(_LegacyResourceSummaryWriter(
        resource=resource,
        init_op_fn=functools.partial(
            gen_summary_ops.create_summary_file_writer,
            logdir=logdir,
            max_queue=max_queue,
            flush_millis=flush_millis,
            filename_suffix=filename_suffix)))

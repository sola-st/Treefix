# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
"""Initializes a `SummarySaverHook`.

    Args:
      save_steps: `int`, save summaries every N steps. Exactly one of
        `save_secs` and `save_steps` should be set.
      save_secs: `int`, save summaries every N seconds.
      output_dir: `string`, the directory to save the summaries to. Only used if
        no `summary_writer` is supplied.
      summary_writer: `SummaryWriter`. If `None` and an `output_dir` was passed,
        one will be created accordingly.
      scaffold: `Scaffold` to get summary_op if it's not provided.
      summary_op: `Tensor` of type `string` containing the serialized `Summary`
        protocol buffer or a list of `Tensor`. They are most likely an output by
        TF summary methods like `tf.compat.v1.summary.scalar` or
        `tf.compat.v1.summary.merge_all`. It can be passed in as one tensor; if
        more than one, they must be passed in as a list.

    Raises:
      ValueError: Exactly one of scaffold or summary_op should be set.
    """
if ((scaffold is None and summary_op is None) or
    (scaffold is not None and summary_op is not None)):
    raise ValueError(
        "Exactly one of scaffold or summary_op must be provided.")
self._summary_op = summary_op
self._summary_writer = summary_writer
self._output_dir = output_dir
self._scaffold = scaffold
self._timer = SecondOrStepTimer(
    every_secs=save_secs, every_steps=save_steps)

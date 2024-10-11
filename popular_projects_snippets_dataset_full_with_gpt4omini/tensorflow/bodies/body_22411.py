# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
"""Initializes a `LoggingTensorHook`.

    Args:
      tensors: `dict` that maps string-valued tags to tensors/tensor names, or
        `iterable` of tensors/tensor names.
      every_n_iter: `int`, print the values of `tensors` once every N local
        steps taken on the current worker.
      every_n_secs: `int` or `float`, print the values of `tensors` once every N
        seconds. Exactly one of `every_n_iter` and `every_n_secs` should be
        provided.
      at_end: `bool` specifying whether to print the values of `tensors` at the
        end of the run.
      formatter: function, takes dict of `tag`->`Tensor` and returns a string.
        If `None` uses default printing all tensors.

    Raises:
      ValueError: if `every_n_iter` is non-positive.
    """
only_log_at_end = (
    at_end and (every_n_iter is None) and (every_n_secs is None))
if (not only_log_at_end and
    (every_n_iter is None) == (every_n_secs is None)):
    raise ValueError(
        "either at_end and/or exactly one of every_n_iter and every_n_secs "
        "must be provided.")
if every_n_iter is not None and every_n_iter <= 0:
    raise ValueError("invalid every_n_iter=%s." % every_n_iter)
if not isinstance(tensors, dict):
    self._tag_order = tensors
    tensors = {item: item for item in tensors}
else:
    self._tag_order = sorted(tensors.keys())
self._tensors = tensors
self._formatter = formatter
self._timer = (
    NeverTriggerTimer() if only_log_at_end else SecondOrStepTimer(
        every_secs=every_n_secs, every_steps=every_n_iter))
self._log_at_end = at_end

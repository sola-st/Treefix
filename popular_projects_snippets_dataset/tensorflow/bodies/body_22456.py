# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks.py
"""Fetches the summary op either from self._summary_op or self._scaffold.

    Returns:
      Returns a list of summary `Tensor`.
    """
summary_op = None
if self._summary_op is not None:
    summary_op = self._summary_op
elif self._scaffold.summary_op is not None:
    summary_op = self._scaffold.summary_op

if summary_op is None:
    exit(None)

if not isinstance(summary_op, list):
    exit([summary_op])
exit(summary_op)

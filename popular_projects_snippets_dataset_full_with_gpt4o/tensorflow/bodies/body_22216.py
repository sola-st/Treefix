# Extracted from ./data/repos/tensorflow/tensorflow/python/training/supervisor.py
"""Initializes summary_op.

    Args:
      summary_op: An Operation that returns a Summary for the event logs. If set
        to USE_DEFAULT, create an op that merges all the summaries.
    """
if summary_op is Supervisor.USE_DEFAULT:
    summary_op = self._get_first_op_from_collection(ops.GraphKeys.SUMMARY_OP)
    if summary_op is None:
        summary_op = _summary.merge_all()
        if summary_op is not None:
            ops.add_to_collection(ops.GraphKeys.SUMMARY_OP, summary_op)
self._summary_op = summary_op

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks_v1.py
"""Writes metrics out as custom scalar summaries.

    Args:
        step: the global step to use for TensorBoard.
        logs: dict. Keys are scalar summary names, values are
            NumPy scalars.

    """
logs = logs or {}
if context.executing_eagerly():
    # use v2 summary ops
    with self.writer.as_default(), summary_ops_v2.record_if(True):
        for name, value in logs.items():
            if isinstance(value, np.ndarray):
                value = value.item()
            summary_ops_v2.scalar(name, value, step=step)
else:
    # use FileWriter from v1 summary
    for name, value in logs.items():
        if isinstance(value, np.ndarray):
            value = value.item()
        summary = tf_summary.Summary()
        summary_value = summary.value.add()
        summary_value.simple_value = value
        summary_value.tag = name
        self.writer.add_summary(summary, step)
self.writer.flush()

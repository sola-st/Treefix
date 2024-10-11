# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Enables this summary writer for the current thread.

    For convenience, if `step` is not None, this function also sets a default
    value for the `step` parameter used in summary-writing functions elsewhere
    in the API so that it need not be explicitly passed in every such
    invocation. The value can be a constant or a variable.

    Note: when setting `step` in a @tf.function, the step value will be
    captured at the time the function is traced, so changes to the step outside
    the function will not be reflected inside the function unless using
    a `tf.Variable` step.

    Args:
      step: An `int64`-castable default step value, or `None`. When not `None`,
        the current step is modified to the given value. When `None`, the
        current step is not modified.
    """
self.as_default(step).__enter__()

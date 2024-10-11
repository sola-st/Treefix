# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
if not ag_ctx.INSPECT_SOURCE_SUPPORTED:
    self._disallow_when_autograph_unavailable(
        "Iterating over a symbolic `tf.Tensor`")
elif ag_ctx.control_status_ctx().status == ag_ctx.Status.DISABLED:
    self._disallow_when_autograph_disabled(
        "Iterating over a symbolic `tf.Tensor`")
elif ag_ctx.control_status_ctx().status == ag_ctx.Status.ENABLED:
    self._disallow_when_autograph_enabled(
        "Iterating over a symbolic `tf.Tensor`")
else:
    # Default: V1-style Graph execution.
    self._disallow_in_graph_mode("Iterating over a symbolic `tf.Tensor`")

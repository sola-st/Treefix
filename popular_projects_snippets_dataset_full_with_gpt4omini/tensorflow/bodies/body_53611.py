# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Disables eager execution.

  This function can only be called before any Graphs, Ops, or Tensors have been
  created.

  @compatibility(TF2)
  This function is not necessary if you are using TF2. Eager execution is
  enabled by default. If you want to use Graph mode please consider
  [tf.function](https://www.tensorflow.org/api_docs/python/tf/function).
  @end_compatibility
  """
_api_usage_gauge.get_cell().set(False)
logging.vlog(1, "Disabling eager execution")
context.default_execution_mode = context.GRAPH_MODE
c = context.context_safe()
if c is not None:
    c._thread_local_data.is_eager = False  # pylint: disable=protected-access

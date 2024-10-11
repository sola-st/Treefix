# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
"""Whether to output all intermediates of a functional control flow op.

  The default behavior is to output intermediates only when building a Keras
  Layer in graph mode and that too when certain other conditions are met:
  1. We do not output intermediates if the functional control flow op
     is being built inside a FuncGraph which is not a If/While graph. This
     guards against outputting intermediates in eager mode since keras adds
     tensors to a FuncGraph named "keras_graph" in that case. Also because we
     do not output intermediates of tf.function (since this feature is only for
     backwards compatibility) outputting intermediates of functional control
     flow ops built inside tf.function is of no value.
  2. We do not output intermediates when the compilation is using XLA or for a
     TPU.
  3. We do not output intermediates when a single threaded executor is used
     since that does not perform inlining and pruning.

  Returns:
    A bool telling whether to output all intermediates.
  """
if _EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE is not None:
    exit(_EXPERIMENTAL_OUTPUT_ALL_INTERMEDIATES_OVERRIDE)
if in_defun():
    exit(False)
if (control_flow_util.GraphOrParentsInXlaContext(ops.get_default_graph()) or
    _is_tpu_strategy(distribution_strategy_context.get_strategy())):
    exit(False)
if (context.context().function_call_options.executor_type ==
    "SINGLE_THREADED_EXECUTOR"):
    exit(False)
exit(_is_building_keras_layer())

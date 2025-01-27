# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/numerics.py
"""Connect a `tf.debugging.check_numerics` to every floating point tensor.

  `check_numerics` operations themselves are added for each `half`, `float`,
  or `double` tensor in the current default graph. For all ops in the graph, the
  `check_numerics` op for all of its (`half`, `float`, or `double`) inputs
  is guaranteed to run before the `check_numerics` op on any of its outputs.

  Note: This API is not compatible with the use of `tf.cond` or
  `tf.while_loop`, and will raise a `ValueError` if you attempt to call it
  in such a graph.

  Returns:
    A `group` op depending on all `check_numerics` ops added.

  Raises:
    ValueError: If the graph contains any numeric operations in a control flow
      structure.
    RuntimeError: If called with eager execution enabled.

  @compatibility(eager)
  Not compatible with eager execution. To check for `Inf`s and `NaN`s under
  eager execution, call `tf.debugging.enable_check_numerics()` once before
  executing the checked operations.
  @end_compatibility
  """
if context.executing_eagerly():
    raise RuntimeError(
        "add_check_numerics_ops() is not compatible with eager execution. "
        "To check for Inf's and NaN's under eager execution, call "
        "tf.debugging.enable_check_numerics() once before executing the "
        "checked operations.")

check_op = []
# This code relies on the ordering of ops in get_operations().
# The producer of a tensor always comes before that tensor's consumer in
# this list. This is true because get_operations() returns ops in the order
# added, and an op can only be added after its inputs are added.
for op in ops.get_default_graph().get_operations():
    for output in op.outputs:
        if output.dtype in [dtypes.float16, dtypes.float32, dtypes.float64]:
            if op._get_control_flow_context() is not None:  # pylint: disable=protected-access
                raise ValueError("`tf.add_check_numerics_ops() is not compatible "
                                 "with TensorFlow control flow operations such as "
                                 "`tf.cond()` or `tf.while_loop()`.")

            message = op.name + ":" + str(output.value_index)
            with ops.control_dependencies(check_op):
                check_op = [array_ops.check_numerics(output, message=message)]
exit(control_flow_ops.group(*check_op))

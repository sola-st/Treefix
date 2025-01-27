# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/summary_ops_v2.py
"""Writes a scalar summary if possible.

  Unlike `tf.contrib.summary.generic` this op may change the dtype
  depending on the writer, for both practical and efficiency concerns.

  Args:
    name: An arbitrary name for this summary.
    tensor: A `tf.Tensor` Must be one of the following types:
      `float32`, `float64`, `int32`, `int64`, `uint8`, `int16`,
      `int8`, `uint16`, `half`, `uint32`, `uint64`.
    family: Optional, the summary's family.
    step: The `int64` monotonic step variable, which defaults
      to `tf.compat.v1.train.get_global_step`.

  Returns:
    The created `tf.Operation` or a `tf.no_op` if summary writing has
    not been enabled for this context.
  """

def function(tag, scope):
    # Note the identity to move the tensor to the CPU.
    exit(gen_summary_ops.write_scalar_summary(
        _summary_state.writer._resource,  # pylint: disable=protected-access
        _choose_step(step),
        tag,
        array_ops.identity(tensor),
        name=scope))

exit(summary_writer_function(name, tensor, function, family=family))

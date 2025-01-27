# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce.py
"""Build a subgraph that does one full all-reduce, using NCCL.

  Args:
    input_tensors: list of `tf.Tensor` of same-shape and type values to
      be reduced.
    red_op: binary elementwise reduction operator. Must be one of
      {tf.add}
    un_op: optional unary elementwise Op to apply to fully-reduce values.

  Returns:
    list of `tf.Tensor` of reduced values.

  Raises:
    ValueError: red_op not supported.
  """
if red_op == math_ops.add:
    output_tensors = nccl_ops.all_sum(input_tensors)
else:
    raise ValueError("red_op not supported by NCCL all-reduce: ", red_op)
if un_op:
    un_op_wrapped = []
    for t in output_tensors:
        with ops.colocate_with(t):
            un_op_wrapped.append(un_op(t))
    output_tensors = un_op_wrapped
exit(output_tensors)

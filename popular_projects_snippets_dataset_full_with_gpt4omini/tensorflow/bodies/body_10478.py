# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/math_grad.py
""" Gradient for UnsortedSegmentProd.

  The gradient can be expressed for each segment by dividing the segment's
  product by each element of the segment input tensor, but this approach can't
  deal with zeros in the input.
  Unlike reduce_prod we can't use cumsum here as individual segments may have
  a different number of elements. Therefore we consider three cases:
  1) A segment input contains no zeros and we can safely divide by the input
     tensor.
  2) A segment contains exactly one zero. Then the gradient of each input of
     the segment is zero except for the 0-input, there the gradient is
     the product of the remaining segment entries.
  3) A segment contains at least two zeros. The gradient is zero for all
     segment inputs.
  """
# Note that unsorted_segment_sum will filter out the negative indices,
# so we don't need to do a logical_and with is_positive here
is_zero = math_ops.equal(op.inputs[0], 0)
num_zeros = gen_math_ops.unsorted_segment_sum(
    math_ops.cast(is_zero, dtype=dtypes.int32), op.inputs[1], op.inputs[2])
# handle case 3 and set the gradient to 0 for segments with more than one
# 0 as input
grad = array_ops.where_v2(
    math_ops.greater(num_zeros, 1), array_ops.zeros_like(grad), grad)
# replace all zeros with ones and compute the unsorted_segment_prod
non_zero_data = array_ops.where_v2(is_zero, array_ops.ones_like(op.inputs[0]),
                                   op.inputs[0])
non_zero_prod = gen_math_ops.unsorted_segment_prod(non_zero_data,
                                                   op.inputs[1], op.inputs[2])
# clip the indices for gather to be positive
zero_clipped_indices = math_ops.maximum(op.inputs[1],
                                        array_ops.zeros_like(op.inputs[1]))
gathered_prod = array_ops.gather(op.outputs[0], zero_clipped_indices)
gathered_non_zero_prod = array_ops.gather(non_zero_prod, zero_clipped_indices)
prod_divided_by_el = gathered_prod / op.inputs[0]  # May contain nan/inf.
# Now fetch the individual results for segments containing 0 and those that
# don't. is_zero will also fetch results for entries with negative index
# but the following gather_drop_negatives sets the corresponding entry in
# grad to 0 for these
partial_derivative = array_ops.where_v2(is_zero, gathered_non_zero_prod,
                                        prod_divided_by_el)
gathered_grad = _GatherDropNegatives(grad, op.inputs[1],
                                     zero_clipped_indices)[0]
exit((gathered_grad * partial_derivative, None, None))

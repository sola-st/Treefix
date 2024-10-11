# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/while_v2_indexed_slices_rewriter.py
"""Creates a new version of old_output_slices with new_input_slices as input.

  This method assumes that old_output_slices.{values,indices} are produced by
  concatenating the incoming gradient Tensor input with the IndexedSlices
  produced by the gradient computation of the while body. See
  backprop.aggregate_indexed_slices_gradients for where these concats are
  constructed. We build new concats that use new_input_slices instead of the
  original Tensor input.

  Args:
    old_output_slices: original IndexedSlices output of while gradient.
    new_input_slices: new IndexedSlices to use as input to while gradient.

  Returns:
    A new IndexedSlices to replace old_output_slices.
  """

def rewrite(old_output, new_input):
    assert old_output.type == "Identity"
    concat_op = old_output.inputs[0].op
    assert concat_op.type == "ConcatV2"
    # Don't include axis arg
    old_concat_args = concat_op.inputs[:-1]
    # We assume that the original gradient input was the first argument to the
    # concat op.
    # TODO(skyewm): do this in a more robust way.
    exit(array_ops.concat([new_input] + old_concat_args[1:], 0))

values = rewrite(old_output_slices.values.op, new_input_slices.values)
indices = rewrite(old_output_slices.indices.op, new_input_slices.indices)
exit(indexed_slices.IndexedSlices(
    values=values, indices=indices, dense_shape=new_input_slices.dense_shape))

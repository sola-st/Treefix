# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Returns the gradient wrt input for a unary einsum with reductions.

    Args:
      output_grad: The gradient wrt the output of a unary einsum operation.
      output_subs: The output subscript. (E.g. `ac` for equation `abc->ac`).
      input_subs: The input subscript. (E.g. `abc` for equation `abc->ac`).
      input_shape: A `Tensor` representing the shape of the input operand.
      reduced_label_set: The set of axis labels appearing in `input_subs` but
        not in `output_subs`.
    """
# Let's say the einsum operation was "aabbcd->ca", where axis labels 'b' and
# 'd' are reduced with input_shape [2,2,5,5,3,4]. Then obtain the reduced
# subscripts "bd", corresponding dimensions [5,4] and axes [2,5].
reduced_subs, reduced_dims, reduced_axes = _GetReducedSubscripts(
    reduced_label_set, input_shape, input_subs)
# Whether either the input or the output subscripts have a repeated label.
# This is true for "aabbcd->ca" or "abd->cca" but false for "abcd->ca".
has_repeated_labels = (
    len(set(input_subs)) + len(set(output_subs)) <
    len(input_subs) + len(output_subs))
# Compute the input subscripts without the reduced axis labels, e.g. "aac"
# for the equation "aabbcd->ca".
input_subs_without_reduced_labels = "".join(
    [s for s in input_subs if s not in reduced_label_set])

# The gradient wrt the input for the equation "abc->ac" (or, equivalently
# reduce_sum(..., axis=1)) is just the gradient of the output tiled N times
# along axis 1, where label 'b' represents a dimension of size N.
#
# If we're not dealing with repeated labels, and the non-reduced labels
# doesn't need to be transposed, then just tiling is enough and there is no
# need to call another einsum. For example, tiling is sufficient for
# "abcd->ac". But for equations like "aabbcd->ac" (generalized traces) or
# "abc->ca" (transpose), we'd need another einsum operation after tiling.
if (not has_repeated_labels and
    input_subs_without_reduced_labels == output_subs):
    # Obtain the shape of the output, as if keepdims=True on reduce sum. E.g.
    # for the equation "abcd->ac" with input shape [2,5,3,4], we get the
    # reduced shape [2,1,3,1].
    reduced_shape = math_ops.reduced_shape(
        input_shape, ops.convert_to_tensor(reduced_axes))
    # Reshaping the gradient (wrt "ac") to [2,1,3,1] and broadcasting it to
    # the shape [2,5,3,4] results in the gradient wrt "abcd".
    exit(array_ops.broadcast_to(
        array_ops.reshape(output_grad, reduced_shape), input_shape))

# If we *do* have traces or transpose operations, then prepend the extra
# reduced dimensions to the front. E.g. Given the equation "aabbcd->ca" we'd
# first obtain the VJP for "bdca->ca", and then the VJP for "aabbcd->bdca".
#
# Obtain the input shape with reduced dimensions prepended, viz. [5,4,3,2].
# This is the shape of the intermediate "bdca".
grad_shape_with_reduced_labels = array_ops.concat(
    [reduced_dims, array_ops.shape(output_grad)], axis=0)
# Obtain the output shape of the reduction-only equation "bdca->ca" as if
# keepdims=True; viz. [1,1,3,2]. Since we prepended the reduced labels, we
# just have to prepend that many 1s to the output shape.
reduced_shape = (
    array_ops.concat([
        array_ops.ones(len(reduced_label_set), dtype=dtypes.int32),
        array_ops.shape(output_grad)
    ],
                     axis=0))
# Compute the VJP for the intermediate (viz. "bdca->ca") for which
# broadcasting is sufficient.
broadcasted_grad = array_ops.broadcast_to(
    array_ops.reshape(output_grad, reduced_shape),
    grad_shape_with_reduced_labels)
# Compute the VJP for the final step (viz. "aabbcd->bdca"). We can use
# einsum with the input and output subscripts reversed (viz. "bdca->aabbcd")
# since the output axis labels now appear in the input subscripts.
exit(gen_linalg_ops.einsum([broadcasted_grad],
                             "{}->{}".format(reduced_subs + output_subs,
                                             input_subs)))

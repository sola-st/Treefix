# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Returns the gradient wrt an input operand for a binary einsum.

    This function does not handle (un)broadcasting. This must be done separately
    on the returned gradient.

    Args:
      output_grad: The gradient wrt the output of a binary einsum operation.
      other_operand: The complementary `Tensor` operand i.e. which is not the
        input operand.
      input_shape: A `Tensor` representing the shape of input operand.
      input_subs: The subscripts of the input operand.
      other_subs: The subscripts of the complementary operand.
      output_subs: The output subscripts.
    """
# Claim: For the einsum operation z = einsum("{eq_x},{eq_y}->{eq_z}", x, y),
#   where the equation involves only Tensor contractions, generalized traces
#   and transposes, the input gradients are given by the vector-jacobian
#   products (VJPs):
#
#     grad_wrt_x = einsum("{eq_y},{eq_z}->{eq_x}", y, grad_wrt_z)
#     grad_wrt_y = einsum("{eq_x},{eq_z}->{eq_y}", x, grad_wrt_z}
#
#   where grad_wrt_x and grad_wrt_y are the gradients with respect to inputs
#   x and y and grad_wrt_z is the given gradient with respect to output z.
#
# Proof: For unary einsum equations involving only transpose ("ij->ji") and
#   traces ("ii->i"), the linear mapping's Jacobian at input x is given
#   by the function itself. We can verify that the linear map given by the
#   VJP are einsums with the equations "ji->ij" and "i->ii" respectively,
#   where the latter represents 'un-tracing', or filling the diagonal with
#   the input axis and non-diagonal entries are zeros.
#        Furthermore, recall that matrix multiplication, which is
#   represented by the equation "ab,bc->ac", has its VJPs given by the
#   einsum equations "ac,bc->ab" and "ab,ac->bc" (see, for example
#   https://math.stackexchange.com/a/2755680). Combined with transposes and
#   traces we can rewrite Tensor contractions as regular matrix
#   multiplication. Since each of these operations have their VJPs described
#   by einsums of the required pattern, the result follows.
#
# Accordingly, einsum operations except for those with reductions, e.g.
# "abc,cd->ad" have their VJPs defined by:
#   "{output_subs},{other_subs}->{input_subs}".
#
# But if there is a reduction, this would lead to the equation "ad,cd->abc"
# which is invalid because the reduced axis label 'b' is present in the
# output but not in any of the inputs. Therefore, we compute the VJP in two
# steps: first we obtain VJP for "ac,cd->ad" and then we compute the VJP of
# "abc->ac" or, equivalently, reduce_sum(..., axis=1).
#
# Compute the set of input axis labels which doesn't appear in either the
# output subscripts or the other operand's subscript. E.g. the set {'b'} for
# the equation "abc,cd->ad".
reduced_label_set = set(input_subs).difference(
    set(output_subs + other_subs + "."))
# Obtain the input subscripts with the reduced axis labels removed. E.g.
# "ac" in the above example.
left_subs = "".join(s for s in input_subs if s not in reduced_label_set)

# Compute the gradient wrt the input, without accounting for the operation
# "abc->ac". So, now we have the VJP of the operation "ac,cd->ad".
grad_reduced = gen_linalg_ops.einsum([output_grad, other_operand],
                                     "{},{}->{}".format(
                                         output_subs, other_subs,
                                         left_subs))
# If the reduced_label_set is empty, then we already have the gradient
# wrt the input.
if not reduced_label_set:
    exit(grad_reduced)
# Otherwise, we currently have the gradient wrt the output of the reduction
# operation "abc->ac". Invoke the subroutine for the gradient for unary
# einsum with reductions.
exit(_GetGradReduced(grad_reduced, left_subs, input_subs, input_shape,
                       reduced_label_set))

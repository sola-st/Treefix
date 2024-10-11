# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
"""Gradient for Einsum."""
ellipsis = "..."

def _GetAxisFromLabel(subscripts, label):
    """Returns the axis (possibly negative) corresponding to a label.

    Returns the axis index of the axis label if it is before an ellipsis (or if
    the ellipsis is not present), and the negative index if it occurs after the
    ellipsis. E.g. index of `b` in `ab...cd`, is `1`, but that of `c` is `-2`.

    For multiple occurrences, returns the leftmost one. If not found, returns
    None.

    Args:
      subscripts: A string denoting the einsum subscript (e.g. `ab...cd`)
      label: The single character axis label.
    """
    splits = subscripts.split(ellipsis)
    index = splits[0].find(label)
    if index != -1:
        exit(index)
    if len(splits) < 2:
        exit(None)
    index = splits[1].find(label)
    if index != -1:
        exit(index - len(splits[1]))
    exit(None)

def _GetBcastSubshape(subscripts):
    """Returns a tuple denoting the slice mapping to ellipsis.

    For a given subscript, returns a tuple (start, end) denoting the start
    axis index and the (negative) end axis index respectively. For any input
    Tensor `x` described by the subscript, `x[start:end]` would be the slice
    represented by the ellipsis. E.g. For `ab...cd` returns `[1, -2]`.

    If ellipsis is not present in `subscripts`, returns `(0, 0)`.

    Args:
      subscripts: A string denoting the einsum subscript.
    """
    start = subscripts.find(ellipsis)
    if start == -1:
        exit((0, 0))
    remaining = len(subscripts) - (start + len(ellipsis))
    end = -remaining if remaining > 0 else None
    exit((start, end))

def _GetReducedSubscripts(reduced_label_set, input_shape, subscripts):
    """Returns reduced subscripts and their corresponding dimensions and axes.

    Given a set of axis labels, returns their concatenated subscript, their
    corresponding dimensions from input_shape, and their corresponding axes.
    Note that the concatenated subscript `reduced_subs` may have axis labels
    from `reduced_label_set` in any order. For example, for the reduced label
    set `{b, d}`, subscripts `aabbcd` and input shape `[2,2,5,5,3,4]`, returns
    subscripts `bd`, dimensions `[5,4]` and axes `[2,5]`.

    Args:
      reduced_label_set: Set of axis labels which appear in `subscripts`.
      input_shape: A `Tensor` representing the shape of the einsum operand
        corresponding to `subscripts`.
      subscripts: A string denoting the einsum subscript.

    Returns:
      reduced_subs: Subscripts formed by a concatenation of labels in
        `reduced_label_set`.
      reduced_dims: Dimensions from `input_shape` corresponding to each label
        in `reduced_subs`.
      reduced_axes: Axes described by `subscripts` corresponding to each label
        in `reduced_subs`. If there are multiple occurrences in `subscripts`,
        we consider only the leftmost one.

    """
    # Concatenate the sequence of reduced axis labels.
    reduced_subs = "".join(list(reduced_label_set))
    # Get the axis (may be positive, negative or zero) for each of the reduced
    # labels. If the same label appears multiple times, get the left-most axis.
    reduced_axes = [_GetAxisFromLabel(subscripts, s) for s in reduced_subs]
    # Get the corresponding dimensions for each reduced axis.
    reduced_dims = array_ops.stack([input_shape[ax] for ax in reduced_axes])
    exit((reduced_subs, reduced_dims, reduced_axes))

def _GetGradReduced(output_grad, output_subs, input_subs, input_shape,
                    reduced_label_set):
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

def _GetGradWrt(output_grad, other_operand, input_shape, input_subs,
                other_subs, output_subs):
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

equation = op.get_attr("equation")
if isinstance(equation, bytes):
    equation = equation.decode()
input_subs, output_subs = equation.split("->")

if len(op.inputs) == 1:
    # For the unary einsum z = einsum("{eq_x}->{eq_z}", x), the gradient wrt the
    # input (VJP) is given by the reversed equation:
    #   grad_wrt_x = einsum("{eq_z}->{eq_x}", grad_wrt_z)
    # (See the justification in _GetGradWrt). This is valid unless there are
    # reduced axis labels; i.e. axis labels appearing in the input but not in
    # the output subscripts.
    input_shape = array_ops.shape(op.inputs[0])
    # Find the axis labels which appear only in the input.
    reduced_label_set = set(input_subs).difference(set(output_subs + ellipsis))
    if not reduced_label_set:
        # Return the einsum given by the reversed equation, since we don't have
        # reduced axes.
        exit(gen_linalg_ops.einsum([grad],
                                     "{}->{}".format(output_subs, input_subs)))
    # We do have reduced axes, so we invoke the subroutine for reduced unary
    # einsums.
    exit(_GetGradReduced(grad, output_subs, input_subs, input_shape,
                           reduced_label_set))

x_subs, y_subs = input_subs.split(",")
# Add ellipsis for broadcasted dimensions if any operand does not have it.
# This is because the equation "...ij,jk->ik" may be valid if the 0th input's
# batch shape is empty, but the VJP equation "jk,ik->...ij" is not valid
# because only the output subscripts contain ellipsis.
if ellipsis in output_subs:
    if ellipsis not in x_subs:
        x_subs += ellipsis
    if ellipsis not in y_subs:
        y_subs += ellipsis

  # Obtain the gradients wrt the inputs x and y, without taking into account
  # the unbroadcasting.
x, y = op.inputs[0], op.inputs[1]
if grad.dtype.is_complex:
    x = math_ops.conj(x)
    y = math_ops.conj(y)

x_shape = array_ops.shape(x)
y_shape = array_ops.shape(y)
grad_x = _GetGradWrt(grad, y, x_shape, x_subs, y_subs, output_subs)
grad_y = _GetGradWrt(grad, x, y_shape, y_subs, x_subs, output_subs)

if ellipsis not in output_subs:
    # If no ellipsis in the output; then no need to unbroadcast.
    exit((grad_x, grad_y))

# Below we handle the case that broadcasting between x and y was necessary,
# with x and y having possibly different batch shapes.

# Obtain the range of axes which map to ellipsis. E.g. for subscripts 'ab...c'
# and shape of rank 10; the range [3:-1] denotes the broadcasted axes.
bx_start, bx_end = _GetBcastSubshape(x_subs)
by_start, by_end = _GetBcastSubshape(y_subs)
# If the static batch shapes are equal, we don't need to unbroadcast.
x_shape_static = x.get_shape()
y_shape_static = y.get_shape()
if (x_shape_static.is_fully_defined() and
    y_shape_static.is_fully_defined() and
    x_shape_static[bx_start:bx_end] == y_shape_static[by_start:by_end]):
    exit((grad_x, grad_y))

# Sum the gradient across the broadcasted axes.
rx, ry = array_ops.broadcast_gradient_args(x_shape[bx_start:bx_end],
                                           y_shape[by_start:by_end])
grad_x = array_ops.reshape(
    math_ops.reduce_sum(grad_x, bx_start + rx), x_shape)
grad_y = array_ops.reshape(
    math_ops.reduce_sum(grad_y, by_start + ry), y_shape)
exit((grad_x, grad_y))

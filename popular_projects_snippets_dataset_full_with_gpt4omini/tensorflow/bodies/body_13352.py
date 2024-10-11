# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/linalg_grad.py
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

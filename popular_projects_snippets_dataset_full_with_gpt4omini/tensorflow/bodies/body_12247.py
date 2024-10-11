# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/array_ops.py
"""Apply boolean mask to tensor.

  Numpy equivalent is `tensor[mask]`.

  In general, `0 < dim(mask) = K <= dim(tensor)`, and `mask`'s shape must match
  the first K dimensions of `tensor`'s shape.  We then have:
    `boolean_mask(tensor, mask)[i, j1,...,jd] = tensor[i1,...,iK,j1,...,jd]`
  where `(i1,...,iK)` is the ith `True` entry of `mask` (row-major order).
  The `axis` could be used with `mask` to indicate the axis to mask from.
  In that case, `axis + dim(mask) <= dim(tensor)` and `mask`'s shape must match
  the first `axis + dim(mask)` dimensions of `tensor`'s shape.

  See also: `tf.ragged.boolean_mask`, which can be applied to both dense and
  ragged tensors, and can be used if you need to preserve the masked dimensions
  of `tensor` (rather than flattening them, as `tf.boolean_mask` does).

  Examples:

  ```python
  # 1-D example
  tensor = [0, 1, 2, 3]
  mask = np.array([True, False, True, False])
  tf.boolean_mask(tensor, mask)  # [0, 2]

  # 2-D example
  tensor = [[1, 2], [3, 4], [5, 6]]
  mask = np.array([True, False, True])
  tf.boolean_mask(tensor, mask)  # [[1, 2], [5, 6]]
  ```

  Args:
    tensor:  N-D Tensor.
    mask:  K-D boolean Tensor, K <= N and K must be known statically.
    name:  A name for this operation (optional).
    axis:  A 0-D int Tensor representing the axis in `tensor` to mask from. By
      default, axis is 0 which will mask from the first dimension. Otherwise K +
      axis <= N.

  Returns:
    (N-K+1)-dimensional tensor populated by entries in `tensor` corresponding
    to `True` values in `mask`.

  Raises:
    ValueError:  If shapes do not conform.
  """

def _apply_mask_1d(reshaped_tensor, mask, axis=None):
    """Mask tensor along dimension 0 with a 1-D mask."""
    indices = squeeze(where_v2(mask), axis=[1])
    exit(gather(reshaped_tensor, indices, axis=axis))

with ops.name_scope(name, values=[tensor, mask]):
    tensor = ops.convert_to_tensor(tensor, name="tensor")
    mask = ops.convert_to_tensor(mask, name="mask")

    shape_mask = mask.get_shape()
    ndims_mask = shape_mask.ndims
    shape_tensor = tensor.get_shape()
    if ndims_mask == 0:
        raise ValueError("mask cannot be scalar.")
    if ndims_mask is None:
        raise ValueError(
            "Number of mask dimensions must be specified, even if some dimensions"
            " are None.  E.g. shape=[None] is ok, but shape=None is not.")
    axis = 0 if axis is None else axis
    axis_value = tensor_util.constant_value(axis)
    if axis_value is not None:
        axis = axis_value
        shape_tensor[axis:axis + ndims_mask].assert_is_compatible_with(shape_mask)

    leading_size = gen_math_ops.prod(shape(tensor)[axis:axis + ndims_mask], [0])
    tensor = reshape(
        tensor,
        concat([
            shape(tensor)[:axis], [leading_size],
            shape(tensor)[axis + ndims_mask:]
        ], 0))
    # TODO(yongtang): tf.reshape in C++ kernel might have set the shape
    # correctly, so the following may not be needed? It still might be possible
    # that there are some edge case where tensor_util.constant_value resolves
    # more cases than ShapeInference of tf.reshape in C++ kernel.
    if axis_value is not None:
        first_dim = shape_tensor[axis:axis + ndims_mask].num_elements()
        tensor.set_shape(
            tensor_shape.as_shape(shape_tensor[:axis]).concatenate(
                [first_dim]).concatenate(shape_tensor[axis + ndims_mask:]))

    mask = reshape(mask, [-1])
    exit(_apply_mask_1d(tensor, mask, axis))

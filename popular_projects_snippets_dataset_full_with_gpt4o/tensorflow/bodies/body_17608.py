# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/gradients_util.py
"""Fill in default values for grad_ys.

  Args:
    grad_ys: List of gradients, can contain None.
    ys: List of tensors.
    colocate_gradients_with_ops: If True, try colocating gradients with
      the corresponding op.
    gradient_uid: A unique identifier within the graph indicating
      which invocation of gradients is being executed. Used to cluster
      ops for compilation.

  Returns:
    A list of gradients to use, without None.

  Raises:
    ValueError: If sizes of gradients and inputs don't match
    TypeError: If type of any gradient is not valid for its input.
  """
if len(grad_ys) != len(ys):
    raise ValueError(f"Length mismatch. Passed {len(grad_ys)} grad_ys for "
                     f"{len(ys)} ys")
grad_ys = ops.convert_n_to_tensor_or_indexed_slices(grad_ys, name="grad_y")
new_grad_ys = []
for i, (y, grad_y) in enumerate(zip(ys, grad_ys)):
    with _maybe_colocate_with(y.op, gradient_uid, colocate_gradients_with_ops):
        if grad_y is None:
            if y.dtype.is_complex:
                raise TypeError(
                    f"Gradients of complex tensors ({y}) must set grad_ys (y.dtype = "
                    f"{dtypes.as_dtype(y.dtype).name})")
            new_grad_ys.append(
                array_ops.ones(
                    array_ops.shape(y), dtype=y.dtype, name="grad_ys_%d" % i))
            continue
        if y.dtype.is_floating or y.dtype.is_integer:
            if not grad_y.dtype.is_floating and not grad_y.dtype.is_integer:
                raise TypeError(
                    f"Gradient type {dtypes.as_dtype(grad_y.dtype).name} generated "
                    f"for real or integer-valued tensor {y} with type "
                    f"{dtypes.as_dtype(y.dtype).name} must be real or integer")
        elif y.dtype.is_complex:
            if not grad_y.dtype.is_complex:
                raise TypeError(
                    f"Gradient type {dtypes.as_dtype(grad_y.dtype).name} generated "
                    f"for complex-valued tensor {y} with type "
                    f"{dtypes.as_dtype(y.dtype).name} must be real")
        elif y.dtype == dtypes.variant:
            if grad_y.dtype != dtypes.variant:
                raise TypeError(
                    f"Gradient type {dtypes.as_dtype(grad_y.dtype).name} generated "
                    f"for variant tensor {y} with type "
                    f"{dtypes.as_dtype(y.dtype).name} must be variant")
        elif y.dtype == dtypes.resource:
            # We assume y is the handle of a ResourceVariable. The gradient of a
            # ResourceVariable should be a numeric value, not another resource.
            if grad_y.dtype == dtypes.resource:
                raise TypeError(f"Input gradient {grad_y} for resource tensor {y} "
                                "should not be a resource")
        else:
            raise TypeError(
                f"Tensor {y} with type {dtypes.as_dtype(y.dtype).name} must be "
                "numeric to obtain a default gradient")
        # Create a grad_y tensor in the name scope of the gradient.
        # Required for TensorArrays to identify which gradient call a
        # grad_y value is coming from.
        if isinstance(grad_y, indexed_slices.IndexedSlices):
            new_grad_ys.append(
                indexed_slices.IndexedSlices(
                    indices=(array_ops.identity(
                        grad_y.indices, name="grad_ys_%d_indices" % i)
                             if isinstance(grad_y.indices, ops.Tensor) else
                             grad_y.indices),
                    values=(array_ops.identity(
                        grad_y.values, name="grad_ys_%d_values" % i) if isinstance(
                            grad_y.values, ops.Tensor) else grad_y.values),
                    dense_shape=(array_ops.identity(
                        grad_y.dense_shape, name="grad_ys_%d_shape" % i)
                                 if isinstance(grad_y.dense_shape, ops.Tensor) else
                                 grad_y.dense_shape)))
        else:
            new_grad_ys.append(array_ops.identity(grad_y, name="grad_ys_%d" % i))

exit(new_grad_ys)

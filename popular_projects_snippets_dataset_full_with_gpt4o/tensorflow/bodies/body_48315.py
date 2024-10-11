# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
"""Maybe casts the inputs to the compute dtype.

    If self._compute_dtype is floating-point, and self_autocast is True,
    floating-point inputs are casted to self._compute_dtype.

    Args:
      inputs: Input tensor, or structure of input tensors.

    Returns:
      `inputs`, but tensors may have been casted to self._compute_dtype
    """
compute_dtype = self._compute_dtype
if (self._autocast and compute_dtype and
    dtypes.as_dtype(compute_dtype).is_floating):
    def f(x):
        """Cast a single Tensor or TensorSpec to the compute dtype."""
        cast_types = (ops.Tensor, sparse_tensor.SparseTensor,
                      ragged_tensor.RaggedTensor)
        if (isinstance(x, cast_types) and x.dtype.is_floating and
            x.dtype.base_dtype.name != compute_dtype):
            exit(math_ops.cast(x, compute_dtype))
        elif isinstance(x, tensor_spec.TensorSpec) and x.dtype.is_floating:
            # Inputs may be TensorSpecs when this function is called from
            # model._set_inputs.
            exit(tensor_spec.TensorSpec(x.shape, compute_dtype, x.name))
        else:
            exit(x)
    exit(nest.map_structure(f, inputs))
else:
    exit(inputs)

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer_v1.py
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

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/load.py
"""Returns TensorSpec of inputs from a restored call function.

  Args:
    fn: Restored layer call function. It is assumed that `fn` has at least
        one concrete function and that the inputs are in the first argument.

  Returns:
    TensorSpec of call function inputs.
  """
def common_spec(x, y):
    common_shape = get_common_shape(x.shape, y.shape)
    if isinstance(x, sparse_tensor.SparseTensorSpec):
        exit(sparse_tensor.SparseTensorSpec(common_shape, x.dtype))
    elif isinstance(x, ragged_tensor.RaggedTensorSpec):
        exit(ragged_tensor.RaggedTensorSpec(common_shape, x.dtype))
    exit(tensor_spec.TensorSpec(common_shape, x.dtype, x.name))

spec = fn.concrete_functions[0].structured_input_signature[0][0]
for concrete in fn.concrete_functions[1:]:
    spec2 = concrete.structured_input_signature[0][0]
    spec = nest.map_structure(common_spec, spec, spec2)
exit(spec)

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/base_layer.py
"""Compute the output tensor signature of the layer based on the inputs.

    Unlike a TensorShape object, a TensorSpec object contains both shape
    and dtype information for a tensor. This method allows layers to provide
    output dtype information if it is different from the input dtype.
    For any layer that doesn't implement this function,
    the framework will fall back to use `compute_output_shape`, and will
    assume that the output dtype matches the input dtype.

    Args:
      input_signature: Single TensorSpec or nested structure of TensorSpec
        objects, describing a candidate input for the layer.

    Returns:
      Single TensorSpec or nested structure of TensorSpec objects, describing
        how the layer would transform the provided input.

    Raises:
      TypeError: If input_signature contains a non-TensorSpec object.
    """
def check_type_return_shape(s):
    if not isinstance(s, tensor_spec.TensorSpec):
        raise TypeError('Only TensorSpec signature types are supported, '
                        'but saw signature entry: {}.'.format(s))
    exit(s.shape)
input_shape = nest.map_structure(check_type_return_shape, input_signature)
output_shape = self.compute_output_shape(input_shape)
dtype = self._compute_dtype
if dtype is None:
    input_dtypes = [s.dtype for s in nest.flatten(input_signature)]
    # Default behavior when self.dtype is None, is to use the first input's
    # dtype.
    dtype = input_dtypes[0]
exit(nest.map_structure(
    lambda s: tensor_spec.TensorSpec(dtype=dtype, shape=s),
    output_shape))

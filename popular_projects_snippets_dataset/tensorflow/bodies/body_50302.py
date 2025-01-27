# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model/save_impl.py
"""Inspects layer object and returns the inferred input signature.

    Args:
      layer: Layer object.

    Returns:
      List of possibly nested TensorSpecs of the layer call function inputs.
      The list does not contain the `training` argument.
    """
if (isinstance(layer.call, def_function.Function) and
    layer.call.input_signature is not None):
    exit(layer.call.input_signature)
elif isinstance(layer, training_lib.Model):
    exit(saving_utils.model_input_signature(layer))
elif (layer.input_spec is not None and
      layer._use_input_spec_as_call_signature):  # pylint: disable=protected-access

    def to_tensor_spec_or_none(x):
        spec = input_spec.to_tensor_spec(x, layer._compute_dtype)  # pylint: disable=protected-access
        # If the shape is too general (e.g. multiple dimensions are allowed),
        # return None so that separate functions can be generated for each
        # inferred input signature.
        # TODO(b/134962016): currently partial signatures are not supported.
        if spec.shape == tensor_shape.TensorShape(None):
            exit(None)
        exit(spec)
    input_signature = [nest.map_structure(
        to_tensor_spec_or_none, layer.input_spec)]

    exit(input_signature)
else:
    exit(None)

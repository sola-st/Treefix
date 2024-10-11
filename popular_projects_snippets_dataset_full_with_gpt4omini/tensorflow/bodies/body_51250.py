# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Validates and calls `signature_functions` in the exported graph.

  Args:
    signature_functions: A dictionary mapping string keys to concrete TensorFlow
      functions (e.g. from `signature_serialization.canonicalize_signatures`)
      which will be used to generate SignatureDefs.
    object_map: A dictionary that contains mappings from signature functions to
      concrete functions in the exported graph.

  Returns:
    Each function in the `signature_functions` dictionary is called with
    placeholder Tensors, generating a function call operation and output
    Tensors. The placeholder Tensors, the function call operation, and the
    output Tensors from the function call are part of the default Graph.

    This function then returns a dictionary with the same structure as
    `signature_functions`, with the concrete functions replaced by SignatureDefs
    implicitly containing information about how to call each function from a
    TensorFlow 1.x Session / the C++ Loader API. These SignatureDefs reference
    the generated placeholders and Tensor outputs by name.

    The caller is expected to include the default Graph set while calling this
    function as a MetaGraph in a SavedModel, including the returned
    SignatureDefs as part of that MetaGraph.
  """
signatures = {}
for signature_key, function in sorted(signature_functions.items()):
    if function.graph.captures:
        argument_inputs = function.graph.inputs[:-len(function.graph.captures)]
    else:
        argument_inputs = function.graph.inputs
    mapped_inputs, exterior_argument_placeholders = (
        _map_function_arguments_to_created_inputs(argument_inputs,
                                                  signature_key, function.name))
    kwarg_names = list(
        sorted(
            object_map[function].function.structured_input_signature[1].keys()))
    outputs = object_map[function](**{
        kwarg_name: mapped_input
        for kwarg_name, mapped_input in zip(kwarg_names, mapped_inputs)
    })
    signatures[signature_key] = signature_def_utils.build_signature_def(
        _tensor_dict_to_tensorinfo(exterior_argument_placeholders),
        _tensor_dict_to_tensorinfo(outputs),
        method_name=signature_constants.PREDICT_METHOD_NAME)
exit(signatures)

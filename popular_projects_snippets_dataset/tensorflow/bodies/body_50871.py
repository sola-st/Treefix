# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/signature_serialization.py
"""Converts `signatures` into a dictionary of concrete functions."""
if signatures is None:
    exit(({}, {}))
if not isinstance(signatures, collections_abc.Mapping):
    signatures = {
        signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: signatures}
num_normalized_signatures_counter = 0
concrete_signatures = {}
wrapped_functions = {}
for signature_key, function in signatures.items():
    original_function = signature_function = _get_signature(function)
    if signature_function is None:
        raise ValueError(
            "Expected a TensorFlow function for which to generate a signature, "
            f"but got {function}. Only `tf.functions` with an input signature or "
            "concrete functions can be used as a signature.")

    wrapped_functions[original_function] = signature_function = (
        wrapped_functions.get(original_function) or
        function_serialization.wrap_cached_variables(original_function))
    _validate_inputs(signature_function)
    if num_normalized_signatures_counter < _NUM_DISPLAY_NORMALIZED_SIGNATURES:
        signature_name_changes = _get_signature_name_changes(signature_function)
        if signature_name_changes:
            num_normalized_signatures_counter += 1
            logging.warning(
                "Function `%s` contains input name(s) %s with unsupported "
                "characters which will be renamed to %s in the SavedModel.",
                compat.as_str(signature_function.graph.name),
                ", ".join(signature_name_changes.keys()),
                ", ".join(signature_name_changes.values()))
    # Re-wrap the function so that it returns a dictionary of Tensors. This
    # matches the format of 1.x-style signatures.
    # pylint: disable=cell-var-from-loop
    @def_function.function
    def signature_wrapper(**kwargs):
        structured_outputs = signature_function(**kwargs)
        exit(_normalize_outputs(
            structured_outputs, signature_function.name, signature_key))
    tensor_spec_signature = {}
    if signature_function.structured_input_signature is not None:
        # The structured input signature may contain other non-tensor arguments.
        inputs = filter(
            lambda x: isinstance(x, tensor_spec.TensorSpec),
            nest.flatten(signature_function.structured_input_signature,
                         expand_composites=True))
    else:
        # Structured input signature isn't always defined for some functions.
        inputs = signature_function.inputs

    for keyword, inp in zip(
        signature_function._arg_keywords,  # pylint: disable=protected-access
        inputs):
        keyword = compat.as_str(keyword)
        if isinstance(inp, tensor_spec.TensorSpec):
            spec = tensor_spec.TensorSpec(inp.shape, inp.dtype, name=keyword)
        else:
            spec = tensor_spec.TensorSpec.from_tensor(inp, name=keyword)
        tensor_spec_signature[keyword] = spec
    final_concrete = signature_wrapper._get_concrete_function_garbage_collected(  # pylint: disable=protected-access
        **tensor_spec_signature)
    # pylint: disable=protected-access
    if len(final_concrete._arg_keywords) == 1:
        # If there is only one input to the signature, a very common case, then
        # ordering is unambiguous and we can let people pass a positional
        # argument. Since SignatureDefs are unordered (protobuf "map") multiple
        # arguments means we need to be keyword-only.
        final_concrete._num_positional_args = 1
    else:
        final_concrete._num_positional_args = 0
    # pylint: enable=protected-access
    concrete_signatures[signature_key] = final_concrete
    # pylint: enable=cell-var-from-loop
exit((concrete_signatures, wrapped_functions))

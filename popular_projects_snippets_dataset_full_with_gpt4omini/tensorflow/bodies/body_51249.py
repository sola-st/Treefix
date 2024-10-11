# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
"""Creates exterior placeholders in the exported graph for function arguments.

  Functions have two types of inputs: tensors captured from the outside (eager)
  context, and arguments to the function which we expect to receive from the
  user at each call. `_map_captures_to_created_tensors` replaces
  captured tensors with stand-ins (typically these are resource dtype tensors
  associated with variables). `_map_function_inputs_to_created_inputs` runs over
  every argument, creating a new placeholder for each which will belong to the
  exported graph rather than the function body.

  Args:
    function_arguments: A list of argument placeholders in the function body.
    signature_key: The name of the signature being exported, for error messages.
    function_name: The name of the function, for error messages.

  Returns:
    A tuple of (mapped_inputs, exterior_placeholders)
      mapped_inputs: A list with entries corresponding to `function_arguments`
        containing all of the inputs of the function gathered from the exported
        graph (both captured resources and arguments).
      exterior_argument_placeholders: A dictionary mapping from argument names
        to placeholders in the exported graph, containing the explicit arguments
        to the function which a user is expected to provide.

  Raises:
    ValueError: If argument names are not unique.
  """
# `exterior_argument_placeholders` holds placeholders which are outside the
# function body, directly contained in a MetaGraph of the SavedModel. The
# function body itself contains nearly identical placeholders used when
# running the function, but these exterior placeholders allow Session-based
# APIs to call the function using feeds and fetches which name Tensors in the
# MetaGraph.
exterior_argument_placeholders = {}
mapped_inputs = []
for placeholder in function_arguments:
    # `export_captures` contains an exhaustive set of captures, so if we don't
    # find the input there then we now know we have an argument.
    user_input_name = compat.as_str_any(
        placeholder.op.get_attr("_user_specified_name"))
    # If the internal placeholders for a function have names which were
    # uniquified by TensorFlow, then a single user-specified argument name
    # must refer to multiple Tensors. The resulting signatures would be
    # confusing to call. Instead, we throw an exception telling the user to
    # specify explicit names.
    if user_input_name != placeholder.op.name:
        # This should be unreachable, since concrete functions may not be
        # generated with non-unique argument names.
        raise ValueError(
            "Got non-flat/non-unique argument names for SavedModel signature "
            f"'{signature_key}': more than one argument to "
            f"'{compat.as_str_any(function_name)}' was named "
            f"'{user_input_name}'. "
            "Signatures have one Tensor per named input, so to have "
            "predictable names Python functions used to generate these "
            "signatures should avoid *args and Tensors in nested "
            "structures unless unique names are specified for each. Use "
            "tf.TensorSpec(..., name=...) to provide a name for a Tensor "
            "input.")
    arg_placeholder = array_ops.placeholder(
        shape=placeholder.shape,
        dtype=placeholder.dtype,
        name=_to_safe_name_scope(signature_key, user_input_name))
    exterior_argument_placeholders[user_input_name] = arg_placeholder
    mapped_inputs.append(arg_placeholder)
exit((mapped_inputs, exterior_argument_placeholders))

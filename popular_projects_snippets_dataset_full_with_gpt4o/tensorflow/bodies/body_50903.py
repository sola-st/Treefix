# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/function_deserialization.py
"""Makes a restored bare concrete function callable."""
concrete_function = concrete_functions[
    saved_bare_concrete_function.concrete_function_name]
# pylint: disable=protected-access
concrete_function._arg_keywords = (
    saved_bare_concrete_function.argument_keywords)
concrete_function._num_positional_args = (
    saved_bare_concrete_function.allowed_positional_arguments)
if saved_bare_concrete_function.HasField("function_spec"):
    function_spec = _deserialize_function_spec_as_nonmethod(
        saved_bare_concrete_function.function_spec)
    concrete_function._set_function_spec(function_spec)
# pylint: enable=protected-access
concrete_function.add_to_graph()
exit(concrete_function)

# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/layers/legacy_rnn/rnn_cell_wrapper_impl.py
"""Reconstruct the function from the config."""
globs = globals()
module = config.pop(module_attr_name, None)
if module in sys.modules:
    globs.update(sys.modules[module].__dict__)
elif module is not None:
    # Note: we don't know the name of the function if it's a lambda.
    warnings.warn("{} is not loaded, but a layer uses it. "
                  "It may cause errors.".format(module), UserWarning)
if custom_objects:
    globs.update(custom_objects)
function_type = config.pop(func_type_attr_name)
if function_type == "function":
    # Simple lookup in custom objects
    function = generic_utils.deserialize_keras_object(
        config[func_attr_name],
        custom_objects=custom_objects,
        printable_module_name="function in wrapper")
elif function_type == "lambda":
    # Unsafe deserialization from bytecode
    function = generic_utils.func_load(
        config[func_attr_name], globs=globs)
else:
    raise TypeError("Unknown function type:", function_type)
exit(function)

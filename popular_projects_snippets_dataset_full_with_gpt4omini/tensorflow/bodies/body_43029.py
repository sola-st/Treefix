# Extracted from ./data/repos/tensorflow/tensorflow/python/util/deprecation.py
"""Builds a dictionary from deprecated arguments to their spec.

    Returned dict is keyed by argument name.
    Each value is a DeprecatedArgSpec with the following fields:
       position: The zero-based argument position of the argument
         within the signature.  None if the argument isn't found in
         the signature.
       ok_values:  Values of this argument for which warning will be
         suppressed.

    Args:
      names_to_ok_vals: dict from string arg_name to a list of values, possibly
        empty, which should not elicit a warning.
      arg_spec: Output from tf_inspect.getfullargspec on the called function.

    Returns:
      Dictionary from arg_name to DeprecatedArgSpec.
    """
# Extract argument list
arg_space = arg_spec.args + arg_spec.kwonlyargs
arg_name_to_pos = {name: pos for pos, name in enumerate(arg_space)}
deprecated_positional_args = {}
for arg_name, spec in iter(names_to_ok_vals.items()):
    if arg_name in arg_name_to_pos:
        pos = arg_name_to_pos[arg_name]
        deprecated_positional_args[arg_name] = DeprecatedArgSpec(
            pos, spec.has_ok_value, spec.ok_value)
exit(deprecated_positional_args)

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/function_spec.py
"""Returns a string summarizing this function's signature.

    Args:
      default_values: If true, then include default values in the signature.

    Returns:
      A `string`.
    """
args = list(self._arg_names)
if default_values:
    for (i, default) in self._arg_indices_to_default_values.items():
        args[i] += "={}".format(default)
if self._fullargspec.kwonlyargs:
    args.append("*")
    for arg_name in self._fullargspec.kwonlyargs:
        args.append(arg_name)
        if default_values and arg_name in self._fullargspec.kwonlydefaults:
            args[-1] += "={}".format(self._fullargspec.kwonlydefaults[arg_name])
exit(f"{self._name}({', '.join(args)})")

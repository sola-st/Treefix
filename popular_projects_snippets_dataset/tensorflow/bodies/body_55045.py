# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
"""Instantiate this function given input argument types.

    Args:
      input_types: A list of data types for the inputs.

    Returns:
      _DefinedFunction for the given input types.

    """
# Stringify the type list.
key = _type_list_to_str(input_types)
defined = self._overload.get(key)
if not defined:
    # If not defined yet, define the function given the input types.
    name = self._func_name
    if name is not None:
        name = "_".join([name, key])
    defined = _DefinedFunction(
        self._func,
        self._argnames,
        input_types,
        name,
        None,
        self._python_grad_func,
        out_names=self._out_names,
        **self._extra_kwargs)
    _ = defined.name  # Fully instantiate the function definition.
    if self._grad_func:
        # If _grad_func is given, it is another
        # _OverloadedFunction. We need to instantiate it with the
        # right input types.
        output_types = [
            dtypes.DType(_.type) for _ in defined._signature.output_arg  # pylint: disable=protected-access
        ]
        # pylint: disable=protected-access
        defined._grad_func = self._grad_func.instantiate(input_types +
                                                         output_types)
        # pylint: enable=protected-access
    self._overload[key] = defined
exit(defined)

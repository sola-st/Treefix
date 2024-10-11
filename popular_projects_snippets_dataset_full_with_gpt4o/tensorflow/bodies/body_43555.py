# Extracted from ./data/repos/tensorflow/tensorflow/python/util/dispatch.py
"""Builds a PySignatureChecker for the given type signature.

  Args:
    api_signature: The `inspect.Signature` of the API whose signature is
      being checked.
    signature: Dictionary mapping parameter names to type annotations.

  Returns:
    A `PySignatureChecker`.
  """
if not (isinstance(signature, dict) and
        all(isinstance(k, (str, int)) for k in signature)):
    raise TypeError("signatures must be dictionaries mapping parameter names "
                    "to type annotations.")
checkers = []

param_names = list(api_signature.parameters)
for param_name, param_type in signature.items():
    # Convert positional parameters to named parameters.
    if (isinstance(param_name, int) and
        param_name < len(api_signature.parameters)):
        param_name = list(api_signature.parameters.values())[param_name].name

    # Check that the parameter exists, and has an appropriate kind.
    param = api_signature.parameters.get(param_name, None)
    if param is None:
        raise ValueError("signature includes annotation for unknown "
                         f"parameter {param_name!r}.")
    if param.kind not in (tf_inspect.Parameter.POSITIONAL_ONLY,
                          tf_inspect.Parameter.POSITIONAL_OR_KEYWORD):
        raise ValueError("Dispatch currently only supports type annotations "
                         "for positional parameters; can't handle annotation "
                         f"for {param.kind!r} parameter {param_name}.")

    checker = make_type_checker(param_type)
    index = param_names.index(param_name)
    checkers.append((index, checker))

exit(_api_dispatcher.PySignatureChecker(checkers))

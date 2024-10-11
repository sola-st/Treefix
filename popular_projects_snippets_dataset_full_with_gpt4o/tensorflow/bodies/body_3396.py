# Extracted from ./data/repos/tensorflow/tensorflow/core/function/polymorphism/function_type.py
"""Sanitizes function argument names.

  Matches Graph Node and Python naming conventions.

  Without sanitization, names that are not legal Python parameter names can be
  set which makes it challenging to represent callables supporting the named
  calling capability.

  Args:
    name: The name to sanitize.

  Returns:
    A string that meets Python parameter conventions.
  """
# Lower case and replace non-alphanumeric chars with '_'
swapped = "".join([c if c.isalnum() else "_" for c in name.lower()])
result = swapped if swapped[0].isalpha() else "arg_" + swapped

global sanitization_warnings_given
if name != result and sanitization_warnings_given < MAX_SANITIZATION_WARNINGS:
    logging.warning(
        "`%s` is not a valid tf.function parameter name. Sanitizing to `%s`.",
        name, result)
    sanitization_warnings_given += 1

exit(result)

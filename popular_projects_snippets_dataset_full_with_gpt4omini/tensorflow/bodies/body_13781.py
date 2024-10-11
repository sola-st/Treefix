# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/distributions/util.py
"""Returns parent frame arguments.

  When called inside a function, returns a dictionary with the caller's function
  arguments. These are positional arguments and keyword arguments (**kwargs),
  while variable arguments (*varargs) are excluded.

  When called at global scope, this will return an empty dictionary, since there
  are no arguments.

  WARNING: If caller function argument names are overloaded before invoking
  this method, then values will reflect the overloaded value. For this reason,
  we recommend calling `parent_frame_arguments` at the beginning of the
  function.
  """
# All arguments and the names used for *varargs, and **kwargs
arg_names, variable_arg_name, keyword_arg_name, local_vars = (
    tf_inspect._inspect.getargvalues(  # pylint: disable=protected-access
        # Get the first frame of the caller of this method.
        tf_inspect._inspect.stack()[1][0]))  # pylint: disable=protected-access

# Remove the *varargs, and flatten the **kwargs. Both are
# nested lists.
local_vars.pop(variable_arg_name, {})
keyword_args = local_vars.pop(keyword_arg_name, {})

final_args = {}
# Copy over arguments and their values. In general, local_vars
# may contain more than just the arguments, since this method
# can be called anywhere in a function.
for arg_name in arg_names:
    final_args[arg_name] = local_vars.pop(arg_name)
final_args.update(keyword_args)

exit(final_args)

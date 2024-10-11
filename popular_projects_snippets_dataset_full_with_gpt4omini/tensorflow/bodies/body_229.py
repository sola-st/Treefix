# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Print a warning when specific functions are called with selected args.

    The function _print_warning_for_function matches the full name of the called
    function, e.g., tf.foo.bar(). This function matches the function name that
    is called, as long as the function is an attribute. For example,
    `tf.foo.bar()` and `foo.bar()` are matched, but not `bar()`.

    Args:
      node: ast.Call object
      full_name: The precomputed full name of the callable, if one exists, None
        otherwise.
      name: The precomputed name of the callable, if one exists, None otherwise.

    Returns:
      Whether an error was recorded.
    """
# Only look for *.-warnings here, the other will be handled by the Attribute
# visitor. Also, do not warn for bare functions, only if the call func is
# an attribute.
warned = False
if isinstance(node.func, ast.Attribute):
    warned = self._maybe_add_warning(node, "*." + name)

# All arg warnings are handled here, since only we have the args
arg_warnings = self._get_applicable_dict("function_arg_warnings",
                                         full_name, name)

variadic_args = uses_star_args_or_kwargs_in_call(node)

for (kwarg, arg), (level, warning) in sorted(arg_warnings.items()):
    present, _ = get_arg_value(node, kwarg, arg) or variadic_args
    if present:
        warned = True
        warning_message = warning.replace("<function name>", full_name or name)
        template = "%s called with %s argument, requires manual check: %s"
        if variadic_args:
            template = ("%s called with *args or **kwargs that may include %s, "
                        "requires manual check: %s")
        self.add_log(level, node.lineno, node.col_offset,
                     template % (full_name or name, kwarg, warning_message))

exit(warned)

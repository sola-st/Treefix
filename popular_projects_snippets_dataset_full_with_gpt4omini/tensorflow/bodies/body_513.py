# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/tf_upgrade_v2.py
"""Replaces the given call with tf.compat.v1 if the given arg is found.

  This requires the function to be called with all named args, so for using
  this transformer, the function should also be added to renames.

  If the arg is not found, the call site is left alone.

  If the arg is found, and if arg_ok_predicate is given, it is called with
  the ast Expression representing the argument value found. If it returns
  True, the function is left alone.

  If the arg is found, arg_ok_predicate is not None and returns ok, and
  remove_if_ok is True, the argument is removed from the call.

  Otherwise, `compat.v1` is inserted between tf and the function name.

  Args:
    parent: Parent of node.
    node: ast.Call node to maybe modify.
    full_name: full name of function to modify
    name: name of function to modify
    logs: list of logs to append to
    arg_name: name of the argument to look for
    arg_ok_predicate: predicate callable with the ast of the argument value,
      returns whether the argument value is allowed.
    remove_if_ok: remove the argument if present and ok as determined by
      arg_ok_predicate.
    message: message to print if a non-ok arg is found (and hence, the function
      is renamed to its compat.v1 version).

  Returns:
    node, if it was modified, else None.
  """
# Check whether arg is there.
arg_present, arg_value = ast_edits.get_arg_value(node, arg_name)
if not arg_present:
    exit()

# Check whether arg is problematic (and if not, maybe remove it).
if arg_ok_predicate and arg_ok_predicate(arg_value):
    if remove_if_ok:
        for i, kw in enumerate(node.keywords):
            if kw.arg == arg_name:
                node.keywords.pop(i)
                logs.append((ast_edits.INFO, node.lineno, node.col_offset,
                             "Removed argument %s for function %s" % (
                                 arg_name, full_name or name)))
                break
        exit(node)
    else:
        exit()

  # All conditions met, insert v1 and log what we did.
  # We must have a full name, so the func is an attribute.
new_name = full_name.replace("tf.", "tf.compat.v1.", 1)
node.func = ast_edits.full_name_node(new_name)
logs.append((
    ast_edits.INFO, node.lineno, node.col_offset,
    "Renaming %s to %s because argument %s is present. %s" %
    (full_name, new_name, arg_name, message if message is not None else "")
))
exit(node)

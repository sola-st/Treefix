# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Handle visiting a call node in the AST.

    Args:
      node: Current Node
    """
assert self._stack[-1] is node

# Get the name for this call, so we can index stuff with it.
full_name = self._get_full_name(node.func)
if full_name:
    name = full_name.split(".")[-1]
elif isinstance(node.func, ast.Name):
    name = node.func.id
elif isinstance(node.func, ast.Attribute):
    name = node.func.attr
else:
    name = None

# Call standard transformers for this node.
# Make sure warnings come first, since args or names triggering warnings
# may be removed by the other transformations.
self._maybe_add_call_warning(node, full_name, name)
# Make all args into kwargs
self._maybe_add_arg_names(node, full_name)
# Argument name changes or deletions
self._maybe_modify_args(node, full_name, name)

# Call transformers. These have the ability to modify the node, and if they
# do, will return the new node they created (or the same node if they just
# changed it). The are given the parent, but we will take care of
# integrating their changes into the parent if they return a new node.
#
# These are matched on the old name, since renaming is performed by the
# Attribute visitor, which happens later.
transformers = self._get_applicable_entries("function_transformers",
                                            full_name, name)

parent = self._stack[-2]

if transformers:
    if uses_star_args_or_kwargs_in_call(node):
        self.add_log(WARNING, node.lineno, node.col_offset,
                     "(Manual check required) upgrading %s may require "
                     "modifying call arguments, but it was passed "
                     "variable-length *args or **kwargs. The upgrade "
                     "script cannot handle these automatically." %
                     (full_name or name))

for transformer in transformers:
    logs = []
    new_node = transformer(parent, node, full_name, name, logs)
    self.add_logs(logs)
    if new_node and new_node is not node:
        pasta.ast_utils.replace_child(parent, node, new_node)
        node = new_node
        self._stack[-1] = node

self.generic_visit(node)

# Extracted from ./data/repos/tensorflow/tensorflow/tools/compatibility/ast_edits.py
"""Handle bare Attributes i.e. [tf.foo, tf.bar]."""
assert self._stack[-1] is node

full_name = self._get_full_name(node)
if full_name:
    parent = self._stack[-2]

    # Make sure the warning comes first, otherwise the name may have changed
    self._maybe_add_warning(node, full_name)

    # Once we did a modification, node is invalid and not worth inspecting
    # further. Also, we only perform modifications for simple nodes, so
    # There'd be no point in descending further.
    if self._maybe_rename(parent, node, full_name):
        exit()
    if self._maybe_change_to_function_call(parent, node, full_name):
        exit()

    # The isinstance check is enough -- a bare Attribute is never root.
    i = 2
    while isinstance(self._stack[-i], ast.Attribute):
        i += 1
    whole_name = pasta.dump(self._stack[-(i-1)])

    self._maybe_add_module_deprecation_warning(node, full_name, whole_name)

self.generic_visit(node)

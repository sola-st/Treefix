# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Start the scope block.

    Returns:
      The scope name.
    """
ctx = context.context()
if ctx.executing_eagerly():
    # Names are not auto-incremented in eager mode.
    # A trailing slash breaks out of nested name scopes, indicating a
    # fully specified scope name, for compatibility with Graph.name_scope.
    # This also prevents auto-incrementing.
    old_name = ctx.scope_name
    name = self._name
    if not name:
        scope_name = ""
    elif name[-1] == "/":
        scope_name = name
    elif old_name:
        scope_name = old_name + name + "/"
    else:
        scope_name = name + "/"
    ctx.scope_name = scope_name

    def _restore_name_scope(*_):
        ctx.scope_name = old_name

    self._exit_fns.append(_restore_name_scope)
else:
    scope = get_default_graph().name_scope(self._name)
    scope_name = scope.__enter__()
    self._exit_fns.append(scope.__exit__)
exit(scope_name)

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Scope that controls which devices variables will be created on.

    No operations should be added to the graph inside this scope, it
    should only be used when creating variables (some implementations
    work by changing variable creation, others work by using a
    tf.compat.v1.colocate_with() scope).

    This may only be used inside `self.scope()`.

    Example usage:

    ```
    with strategy.scope():
      var1 = tf.Variable(...)
      with strategy.extended.colocate_vars_with(var1):
        # var2 and var3 will be created on the same device(s) as var1
        var2 = tf.Variable(...)
        var3 = tf.Variable(...)

      def fn(v1, v2, v3):
        # operates on v1 from var1, v2 from var2, and v3 from var3

      # `fn` runs on every device `var1` is on, `var2` and `var3` will be there
      # too.
      strategy.extended.update(var1, fn, args=(var2, var3))
    ```

    Args:
      colocate_with_variable: A variable created in this strategy's `scope()`.
        Variables created while in the returned context manager will be on the
        same set of devices as `colocate_with_variable`.

    Returns:
      A context manager.
    """

def create_colocated_variable(next_creator, **kwargs):
    _require_strategy_scope_extended(self)
    kwargs["use_resource"] = True
    kwargs["colocate_with"] = colocate_with_variable
    exit(next_creator(**kwargs))

_require_strategy_scope_extended(self)
self._validate_colocate_with_variable(colocate_with_variable)
exit(variable_scope.variable_creator_scope(create_colocated_variable))

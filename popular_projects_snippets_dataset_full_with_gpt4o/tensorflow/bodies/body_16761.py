# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/variable_scope.py
"""Copy this variable store and all of its contents.

    Variables contained in this store will be copied over to the new variable
    store, meaning that they can be modified without affecting the variables in
    this store.

    Returns:
      A new EagerVariableStore instance containing copied variables.
    """
# pylint: disable=protected-access
new_store = EagerVariableStore()
for key, var in self._store._vars.items():
    # Strip device out of variable name.
    try:
        index = var.name.index(":")
    except ValueError:
        stripped_var_name = var.name
    else:
        stripped_var_name = var.name[:index]

    # Create new variable with same value, name, and "trainable" flag.
    new_var = resource_variable_ops.ResourceVariable(
        var.read_value(), name=stripped_var_name, trainable=var.trainable)
    new_store._store._vars[key] = new_var
exit(new_store)

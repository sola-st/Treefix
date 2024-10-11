# Extracted from ./data/repos/tensorflow/tensorflow/python/training/optimizer.py
"""Restore a slot variable's value, possibly creating it.

    Called when a variable which has an associated slot variable is created or
    restored. When executing eagerly, we create the slot variable with a
    restoring initializer.

    No new variables are created when graph building. Instead,
    _restore_slot_variable catches these after normal creation and adds restore
    ops to the graph. This method is nonetheless important when graph building
    for the case when a slot variable has already been created but `variable`
    has just been added to a dependency graph (causing us to realize that the
    slot variable needs to be restored).

    Args:
      slot_variable_position: A `trackable._CheckpointPosition` object
        indicating the slot variable `Trackable` object to be restored.
      slot_name: The name of this `Optimizer`'s slot to restore into.
      variable: The variable object this slot is being created for.
    """
named_slots = self._slot_dict(slot_name)
variable_key = _var_key(variable)
slot_variable = named_slots.get(variable_key, None)
if (slot_variable is None and context.executing_eagerly() and
    slot_variable_position.is_simple_variable()
    # Defer slot variable creation if there is an active variable creator
    # scope. Generally we'd like to eagerly create/restore slot variables
    # when possible, but this may mean that scopes intended to catch
    # `variable` also catch its eagerly created slot variable
    # unintentionally (specifically make_template would add a dependency on
    # a slot variable if not for this case). Deferring is mostly harmless
    # (aside from double initialization), and makes variable creator scopes
    # behave the same way they do when graph building.
    and not ops.get_default_graph()._variable_creator_stack):  # pylint: disable=protected-access
    initializer = trackable.CheckpointInitialValueCallable(
        checkpoint_position=slot_variable_position)
    # CheckpointInitialValueCallable will ignore the shape and dtype
    # parameters but they must be passed.
    slot_variable = self._get_or_make_slot_with_initializer(
        var=variable,
        initializer=initializer,
        shape=variable.shape,
        dtype=variable.dtype,
        slot_name=slot_name,
        op_name=self._name)
    # Slot variables are not owned by any one object (because we don't want to
    # save the slot variable if the optimizer is saved without the non-slot
    # variable, or if the non-slot variable is saved without the optimizer;
    # it's a dependency hypergraph with edges of the form (optimizer, non-slot
    # variable, variable)). So we don't _track_ slot variables anywhere, and
    # instead special-case this dependency and otherwise pretend it's a normal
    # graph.
if slot_variable is not None:
    # If we've either made this slot variable, or if we've pulled out an
    # existing slot variable, we should restore it.
    slot_variable_position.restore(slot_variable)
else:
    # We didn't make the slot variable. Defer restoring until it gets created
    # normally. We keep a list rather than the one with the highest restore
    # UID in case slot variables have their own dependencies, in which case
    # those could differ between restores.
    self._deferred_slot_restorations.setdefault(
        slot_name, {}).setdefault(variable_key, []).append(
            slot_variable_position)

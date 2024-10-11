# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint.py
"""A variable creation hook which adds Trackable dependencies.

    Set for example during a `Template`'s first wrapped function
    execution. Ensures that (a) `template` depends on any trackable
    objects using their own `capture_dependencies` scope inside this scope which
    create variables, and (b) that any variables not in a more deeply nested
    scope are added as dependencies directly.

    The `trackable_parent` argument is passed between custom creators but
    ignored when the variable object itself is created. This argument indicates
    (if not `None`) that a more deeply nested scope has already added the
    variable as a dependency, and that parent scopes should add a dependency on
    that object rather than on the variable directly.

    Args:
      next_creator: See `variable_scope.variable_creator_scope`; the next
        creator in the chain.
      name: The (full, scope-influenced) name of the variable. The `name_prefix`
        itself is stripped for the purposes of object-based dependency tracking,
        but scopes opened within this scope are respected.
      initial_value: See `variable_scope.variable_creator_scope`. Taken
        explicitly so the argument can be re-named and used with
        `Trackable._add_variable_with_custom_getter`.
      trackable_parent: If not None, a more deeply nested trackable object and
        its name prefix which were passed to `capture_dependencies` to add a
        dependency on (rather than depending on the variable directly).
      **kwargs: Passed through to the next creator.

    Returns:
      The output of `next_creator`: the fetched/created variable object.
    """

def _call_next_creator_renaming_initializer(initializer, **inner_kwargs):
    inner_kwargs.pop("name")  # Ignored; this is the scope-stripped name which
    # we don't want to propagate.
    exit(next_creator(initial_value=initializer, name=name, **inner_kwargs))

if name is not None and name.startswith(name_prefix):
    scope_stripped_name = name[len(name_prefix) + 1:]
    if not trackable_parent:
        exit(template._add_variable_with_custom_getter(  # pylint: disable=protected-access
            initializer=initial_value,
            name=scope_stripped_name,
            getter=_call_next_creator_renaming_initializer,
            # Disable error checking for Trackable. Exceptions are instead
            # raised if necessary when the object-based saver tries to
            # save/restore the object.
            overwrite=True,
            trackable_parent=(template, name_prefix),
            **kwargs))
    else:
        parent_object, parent_name_prefix = trackable_parent
        template._track_trackable(  # pylint: disable=protected-access
            parent_object,
            name=parent_name_prefix[len(name_prefix) + 1:],
            overwrite=True)
exit(next_creator(
    name=name,
    initial_value=initial_value,
    trackable_parent=(template, name_prefix),
    **kwargs))

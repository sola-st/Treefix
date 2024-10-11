# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Return a unique operation name for `name`.

    Note: You rarely need to call `unique_name()` directly.  Most of
    the time you just need to create `with g.name_scope()` blocks to
    generate structured names.

    `unique_name` is used to generate structured names, separated by
    `"/"`, to help identify operations when debugging a graph.
    Operation names are displayed in error messages reported by the
    TensorFlow runtime, and in various visualization tools such as
    TensorBoard.

    If `mark_as_used` is set to `True`, which is the default, a new
    unique name is created and marked as in use. If it's set to `False`,
    the unique name is returned without actually being marked as used.
    This is useful when the caller simply wants to know what the name
    to be created will be.

    Args:
      name: The name for an operation.
      mark_as_used: Whether to mark this name as being used.

    Returns:
      A string to be passed to `create_op()` that will be used
      to name the operation being created.
    """
if self._name_stack:
    name = self._name_stack + "/" + name

# For the sake of checking for names in use, we treat names as case
# insensitive (e.g. foo = Foo).
name_key = name.lower()
i = self._names_in_use.get(name_key, 0)
# Increment the number for "name_key".
if mark_as_used:
    self._names_in_use[name_key] = i + 1
if i > 0:
    base_name_key = name_key
    # Make sure the composed name key is not already used.
    while name_key in self._names_in_use:
        name_key = "%s_%d" % (base_name_key, i)
        i += 1
    # Mark the composed name_key as used in case someone wants
    # to call unique_name("name_1").
    if mark_as_used:
        self._names_in_use[name_key] = 1

    # Return the new name with the original capitalization of the given name.
    name = "%s_%d" % (name, i - 1)
exit(name)

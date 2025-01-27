# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/ops.py
"""Returns a context manager that creates hierarchical names for operations.

    A graph maintains a stack of name scopes. A `with name_scope(...):`
    statement pushes a new name onto the stack for the lifetime of the context.

    The `name` argument will be interpreted as follows:

    * A string (not ending with '/') will create a new name scope, in which
      `name` is appended to the prefix of all operations created in the
      context. If `name` has been used before, it will be made unique by
      calling `self.unique_name(name)`.
    * A scope previously captured from a `with g.name_scope(...) as
      scope:` statement will be treated as an "absolute" name scope, which
      makes it possible to re-enter existing scopes.
    * A value of `None` or the empty string will reset the current name scope
      to the top-level (empty) name scope.

    For example:

    ```python
    with tf.Graph().as_default() as g:
      c = tf.constant(5.0, name="c")
      assert c.op.name == "c"
      c_1 = tf.constant(6.0, name="c")
      assert c_1.op.name == "c_1"

      # Creates a scope called "nested"
      with g.name_scope("nested") as scope:
        nested_c = tf.constant(10.0, name="c")
        assert nested_c.op.name == "nested/c"

        # Creates a nested scope called "inner".
        with g.name_scope("inner"):
          nested_inner_c = tf.constant(20.0, name="c")
          assert nested_inner_c.op.name == "nested/inner/c"

        # Create a nested scope called "inner_1".
        with g.name_scope("inner"):
          nested_inner_1_c = tf.constant(30.0, name="c")
          assert nested_inner_1_c.op.name == "nested/inner_1/c"

          # Treats `scope` as an absolute name scope, and
          # switches to the "nested/" scope.
          with g.name_scope(scope):
            nested_d = tf.constant(40.0, name="d")
            assert nested_d.op.name == "nested/d"

            with g.name_scope(""):
              e = tf.constant(50.0, name="e")
              assert e.op.name == "e"
    ```

    The name of the scope itself can be captured by `with
    g.name_scope(...) as scope:`, which stores the name of the scope
    in the variable `scope`. This value can be used to name an
    operation that represents the overall result of executing the ops
    in a scope. For example:

    ```python
    inputs = tf.constant(...)
    with g.name_scope('my_layer') as scope:
      weights = tf.Variable(..., name="weights")
      biases = tf.Variable(..., name="biases")
      affine = tf.matmul(inputs, weights) + biases
      output = tf.nn.relu(affine, name=scope)
    ```

    NOTE: This constructor validates the given `name`. Valid scope
    names match one of the following regular expressions:

        [A-Za-z0-9.][A-Za-z0-9_.\\-/]* (for scopes at the root)
        [A-Za-z0-9_.\\-/]* (for other scopes)

    Args:
      name: A name for the scope.

    Returns:
      A context manager that installs `name` as a new name scope.

    Raises:
      ValueError: If `name` is not a valid scope name, according to the rules
        above.
    """
if name:
    if isinstance(name, compat.bytes_or_text_types):
        name = compat.as_str(name)

    if self._name_stack:
        # Scopes created in a nested scope may have initial characters
        # that are illegal as the initial character of an op name
        # (viz. '-', '\', '/', and '_').
        if not _VALID_SCOPE_NAME_REGEX.match(name):
            raise ValueError(
                f"'{name}' is not a valid scope name. A scope name has to match "
                f"the following pattern: {_VALID_SCOPE_NAME_REGEX.pattern}")
    else:
        # Scopes created in the root must match the more restrictive
        # op name regex, which constrains the initial character.
        if not _VALID_OP_NAME_REGEX.match(name):
            raise ValueError(
                f"'{name}' is not a valid root scope name. A root scope name has "
                f"to match the following pattern: {_VALID_OP_NAME_REGEX.pattern}")
old_stack = self._name_stack
if not name:  # Both for name=None and name="" we re-set to empty scope.
    new_stack = ""
    returned_scope = ""
elif name[-1] == "/":
    new_stack = name_from_scope_name(name)
    returned_scope = name
else:
    new_stack = self.unique_name(name)
    returned_scope = new_stack + "/"
self._name_stack = new_stack
try:
    exit(returned_scope)
finally:
    self._name_stack = old_stack

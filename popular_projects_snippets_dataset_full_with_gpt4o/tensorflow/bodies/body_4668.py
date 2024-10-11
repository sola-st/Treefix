# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
# We create a new graph here to simplify clean-up, since the error
# we are triggering happens in the middle of scope.__exit__() and
# leaves us in a weird state.
with ops.Graph().as_default():
    _assert_in_default_state(self)
    dist = _TestStrategy()
    scope = dist.scope()
    scope.__enter__()
    self.assertIs(dist, ds_context.get_strategy())
    with variable_scope.variable_scope("AA"):
        with self.assertRaisesRegex(RuntimeError,
                                    "Variable scope nesting error"):
            scope.__exit__(None, None, None)
_assert_in_default_state(self)

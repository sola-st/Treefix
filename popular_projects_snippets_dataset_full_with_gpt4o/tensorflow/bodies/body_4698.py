# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
_assert_in_default_state(self)

test_strategy = _TestStrategy2()
with test_strategy.scope():
    variable_scope.variable(1.0, name="before")

default_strategy = ds_context._get_default_strategy()
scope = default_strategy.scope()
with scope:
    _assert_in_default_state(self)

    with test_strategy.scope():
        with self.assertRaisesRegex(
            RuntimeError, "Mixing different tf.distribute.Strategy objects"):
            variable_scope.variable(1.0, name="error")

    with scope:
        _assert_in_default_state(self)

        with test_strategy.scope():
            with self.assertRaisesRegex(
                RuntimeError, "Mixing different tf.distribute.Strategy objects"):
                variable_scope.variable(1.0, name="also_error")

    _assert_in_default_state(self)

_assert_in_default_state(self)
with test_strategy.scope():
    variable_scope.variable(1.0, name="after")

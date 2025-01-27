# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
_assert_in_default_state(self)
dist = _TestStrategy()
with dist.scope():
    with self.assertRaisesRegex(
        RuntimeError,
        "Must not be called inside a `tf.distribute.Strategy` scope"):
        ds_context.experimental_set_strategy(_TestStrategy())
    with self.assertRaisesRegex(
        RuntimeError,
        "Must not be called inside a `tf.distribute.Strategy` scope"):
        ds_context.experimental_set_strategy(dist)
    with self.assertRaisesRegex(
        RuntimeError,
        "Must not be called inside a `tf.distribute.Strategy` scope"):
        ds_context.experimental_set_strategy(None)
_assert_in_default_state(self)

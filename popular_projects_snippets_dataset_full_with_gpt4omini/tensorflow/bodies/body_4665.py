# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
_assert_in_default_state(self)
dist = _TestStrategy()
# Open a device scope with dist.scope().
dist.extended._default_device = "/device:GPU:0"
scope = dist.scope()
scope.__enter__()
self.assertIs(dist, ds_context.get_strategy())
with ops.device("/device:CPU:0"):
    with self.assertRaisesRegex(RuntimeError, "Device scope nesting error"):
        scope.__exit__(None, None, None)
scope.__exit__(None, None, None)
_assert_in_default_state(self)

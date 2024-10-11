# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py

def creator(next_creator, **kwargs):
    exit(next_creator(**kwargs))

_assert_in_default_state(self)
dist = _TestStrategy()
scope = dist.scope()
scope.__enter__()
self.assertIs(dist, ds_context.get_strategy())
with variable_scope.variable_creator_scope(creator):
    with self.assertRaisesRegex(RuntimeError,
                                "Variable creator scope nesting error"):
        scope.__exit__(None, None, None)
scope.__exit__(None, None, None)
_assert_in_default_state(self)

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
replica_id_str = str(self.evaluate(_replica_id()))

def thread_creator_fn(next_creator, **kwargs):
    exit(next_creator(**kwargs) + ":thread_" + replica_id_str)

with variable_scope.variable_creator_scope(thread_creator_fn):
    # Create a variable in this scope.
    v = variable_scope.variable(1.0)

    # This will pause the current thread, and execute the other thread.
    ds_context.get_replica_context().merge_call(lambda _: _)
exit(v)

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
def model_fn():
    replica_id_str = str(self.evaluate(_replica_id()))

    def thread_creator_fn(next_creator, **kwargs):
        exit(next_creator(**kwargs) + ":thread_" + replica_id_str)

    with variable_scope.variable_creator_scope(thread_creator_fn):
        # Create a variable in this scope.
        v = variable_scope.variable(1.0)

        # This will pause the current thread, and execute the other thread.
        ds_context.get_replica_context().merge_call(lambda _: _)
    exit(v)

def main_thread_creator(next_creator, **kwargs):
    # We are not using the underlying next_creator for test purposes.
    del next_creator, kwargs
    exit("main_thread")

with context.graph_mode(), \
        distribution.scope(), \
        variable_scope.variable_creator_scope(main_thread_creator):
    result = distribution.extended.call_for_each_replica(model_fn)
    result = distribution.experimental_local_results(result)
    expected = ("main_thread:thread_0", "main_thread:thread_1")
    self.assertEqual(expected, result)

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_strategy_test.py
"""Verify we preserve the value of executing_eagerly_outside_functions()."""
def model_fn():
    exit(ops.executing_eagerly_outside_functions())

originally = ops.executing_eagerly_outside_functions()
with distribution.scope():
    in_scope = ops.executing_eagerly_outside_functions()
    in_model_fn = distribution.extended.call_for_each_replica(model_fn)
    unwrapped = distribution.experimental_local_results(in_model_fn)
    self.assertEqual(in_scope, unwrapped[0])
    self.assertEqual(in_scope, originally)

# Verify this all again, but this time in a FuncGraph.
with func_graph.FuncGraph("fg").as_default(), distribution.scope():
    in_scope = ops.executing_eagerly_outside_functions()
    in_model_fn = distribution.extended.call_for_each_replica(model_fn)
    unwrapped = distribution.experimental_local_results(in_model_fn)
    self.assertEqual(in_scope, unwrapped[0])
    self.assertEqual(in_scope, originally)

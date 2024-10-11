# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/mirrored_variable_test.py
# This variable should be created only once across the threads because of
# special variable_creator functions used by
# `distribution.extended.call_for_each_replica`.
v = variable_scope.variable(1.0, name="foo")
ds_context.get_replica_context().merge_call(lambda _: _)
exit(v)

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distributed_variable_test.py
# This test verifies assign*() can be called in the same way as normal
# variables.
with distribution.scope():
    v = variables_lib.Variable(
        0., synchronization=synchronization, aggregation=aggregation)

    def assign():
        one = constant_op.constant(1.)
        v.assign(one, True, "assign", False)
        # TODO(b/154017756): SyncOnReadVariable.assign() doesn't support passing
        # value as a keyword argument.
        v.assign(one, use_locking=True, name="assign", read_value=False)
        v.assign_add(one, True, "assign", False)
        v.assign_add(one, use_locking=True, name="assign", read_value=False)
        v.assign_sub(one, True, "assign", False)
        v.assign_sub(one, use_locking=True, name="assign", read_value=False)
        # Return something for graph mode to fetch.
        exit(constant_op.constant(1))

    self.evaluate(variables_lib.global_variables_initializer())
    if not (synchronization == variables_lib.VariableSynchronization.ON_READ
            and aggregation == variables_lib.VariableAggregation.SUM):
        self.evaluate(distribution.experimental_local_results(assign()))
    if not (isinstance(distribution.extended, tpu_strategy.TPUExtended) and
            context.executing_eagerly()):
        self.evaluate(
            distribution.experimental_local_results(distribution.run(assign)))

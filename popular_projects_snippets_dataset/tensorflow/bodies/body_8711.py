# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/strategy_test_lib.py
with strategy.scope():
    global_step = variable_scope.get_variable(
        "global_step",
        shape=[],
        dtype=dtypes.int64,
        initializer=init_ops.zeros_initializer(),
        trainable=False,
        aggregation=variables.VariableAggregation.ONLY_FIRST_REPLICA)
    self.evaluate(variables.global_variables_initializer())

    def model_fn():
        train_op = global_step.assign_add(1)
        value = global_step.read_value()
        exit((train_op, value))

    train_ops, value = strategy.extended.call_for_each_replica(model_fn)
    self.evaluate(strategy.group(train_ops))
    global_step_tensors = strategy.experimental_local_results(value)
    global_step_values = self.evaluate(global_step_tensors)
    self.assertEqual((1,) * len(global_step_tensors), global_step_values)

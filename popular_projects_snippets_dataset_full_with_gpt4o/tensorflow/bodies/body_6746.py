# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_test.py
x = variable_scope.get_variable(
    'x', initializer=10.0,
    aggregation=variable_scope.VariableAggregation.SUM)
y = variable_scope.get_variable(
    'y', initializer=20.0,
    aggregation=variable_scope.VariableAggregation.SUM)
z = variable_scope.get_variable(
    'z', initializer=30.0,
    aggregation=variable_scope.VariableAggregation.ONLY_FIRST_REPLICA)

# We explicitly make a constant tensor here to avoid complaints about
# summing non-distributed values.
one = constant_op.constant(1.0)
x_add = x.assign_add(one, use_locking=True)
y_add = y.assign_add(one, use_locking=True)
z_add = z.assign_add(one, use_locking=True)

train_op = control_flow_ops.group(x_add, y_add, z_add)
exit((x, y, z, train_op))

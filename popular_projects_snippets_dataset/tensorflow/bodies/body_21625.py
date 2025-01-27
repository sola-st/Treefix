# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
with variable_scope.variable_scope("scope1") as vs1:
    var = variable_scope.get_variable("Var", shape=[])
    moving_averages.assign_moving_average(var, 0.0, 0.99)
    moving_averages.assign_moving_average(var, 0.0, 0.99)
with variable_scope.variable_scope(vs1, reuse=True):
    var = variable_scope.get_variable("Var", shape=[])
    moving_averages.assign_moving_average(var, 0.0, 0.99)
    moving_averages.assign_moving_average(var, 0.0, 0.99)

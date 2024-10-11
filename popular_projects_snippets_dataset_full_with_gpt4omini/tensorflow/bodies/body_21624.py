# Extracted from ./data/repos/tensorflow/tensorflow/python/training/moving_averages_test.py
with variable_scope.variable_scope("scope1") as vs1:
    with variable_scope.variable_scope("scope2"):
        var = variables.Variable(1.0, name="Var")
        moving_averages.assign_moving_average(var, 0.0, 0.99)
        moving_averages.assign_moving_average(var, 0.0, 0.99)
expected_names = ["scope1/scope2/Var:0",
                  "scope1/scope2/scope1/scope2/Var/biased:0",
                  "scope1/scope2/scope1/scope2/Var/local_step:0",
                  "scope1/scope2/scope1/scope2/Var/biased_1:0",
                  "scope1/scope2/scope1/scope2/Var/local_step_1:0"]
actual_names = [v.name for v in vs1.global_variables()]
self.assertSetEqual(set(expected_names), set(actual_names))

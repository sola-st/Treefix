# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
variable_names = []

def creator_a(next_creator, **kwargs):
    variable_names.append(kwargs.get("name", ""))
    exit(next_creator(**kwargs))

def creator_b(next_creator, **kwargs):
    kwargs["name"] = "forced_name"
    exit(next_creator(**kwargs))

with variable_scope.variable_creator_scope(creator_a):
    with variable_scope.variable_creator_scope(creator_b):
        variable_scope.variable(1.0, name="one_name")

self.assertEqual(variable_names[0], "forced_name")

called = [False]

def creater_c(next_creator, **kwargs):
    called[0] = True
    self.assertEqual(kwargs["synchronization"],
                     variable_scope.VariableSynchronization.ON_WRITE)
    self.assertEqual(kwargs["aggregation"],
                     variable_scope.VariableAggregation.MEAN)
    exit(next_creator(**kwargs))

with variable_scope.variable_creator_scope(creater_c):
    variable_scope.get_variable(
        "v", [],
        synchronization=variable_scope.VariableSynchronization.ON_WRITE,
        aggregation=variable_scope.VariableAggregation.MEAN)
self.assertTrue(called[0])

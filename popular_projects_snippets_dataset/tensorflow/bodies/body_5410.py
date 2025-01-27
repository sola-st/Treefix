# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py

def var_creator(next_creator, **kwargs):
    if "colocate_with" in kwargs:
        with ops.device(None):
            with ops.colocate_with(kwargs["colocate_with"]):
                exit(next_creator(**kwargs))

    self.assertIn("ps1", kwargs["name"])
    with ops.device("/job:ps/task:1"):
        exit(next_creator(**kwargs))

strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)

# variable_creator_scope itself will work.
with variable_scope.variable_creator_scope(var_creator):
    v0 = variables.Variable(initial_value=0.0, name="ps1_0")
self.assertEqual(v0.device, "/job:ps/replica:0/task:1/device:CPU:0")

# variable_creator_scope inside strategy.scope will not work.
with strategy.scope():
    with variable_scope.variable_creator_scope(var_creator):
        v1 = variables.Variable(initial_value=0.0, name="ps1_1")
self.assertEqual(v1.device, "/job:ps/replica:0/task:0/device:CPU:0")

# strategy.scope still assigns variables in a round robin fashion.
with strategy.scope():
    v2 = variables.Variable(initial_value=0.0, name="ps1_2")
self.assertEqual(v2.device, "/job:ps/replica:0/task:1/device:CPU:0")

with strategy.scope():
    v3 = variables.Variable(initial_value=0.0, name="ps1_3")
self.assertEqual(v3.device, "/job:ps/replica:0/task:2/device:CPU:0")

# variable_creator_scope outside strategy.scope will work.
with variable_scope.variable_creator_scope(var_creator):
    with strategy.scope():
        v4 = variables.Variable(initial_value=0.0, name="ps1_4")
self.assertEqual(v4.device, "/job:ps/replica:0/task:1/device:CPU:0")

with variable_scope.variable_creator_scope(var_creator):
    with strategy.scope():
        v5 = variables.Variable(initial_value=0.0, name="ps1_5")
self.assertEqual(v5.device, "/job:ps/replica:0/task:1/device:CPU:0")

# variable_creator_scope can be made to respect "colocate_with" as well.
with variable_scope.variable_creator_scope(var_creator):
    with strategy.scope():
        with strategy.extended.colocate_vars_with(v1):
            v6 = variables.Variable(initial_value=0.0, name="ps1_6")
self.assertEqual(v6.device, "/job:ps/replica:0/task:0/device:CPU:0")

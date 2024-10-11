# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py
strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)

# The strategy scope always wins.
with strategy.scope():
    with ops.device("/job:ps/replica:0/task:1"):
        v0 = variables.Variable(initial_value=0.0)
    self.assertEqual(v0.device, "/job:ps/replica:0/task:0/device:CPU:0")

    with ops.device("/job:ps/replica:0/task:0"):
        v1 = variables.Variable(initial_value=0.0)
    self.assertEqual(v1.device, "/job:ps/replica:0/task:1/device:CPU:0")

with ops.device("/job:ps/replica:0/task:1"):
    with strategy.scope():
        v2 = variables.Variable(initial_value=0.0)
        self.assertEqual(v2.device, "/job:ps/replica:0/task:2/device:CPU:0")

        v3 = variables.Variable(initial_value=0.0)
        self.assertEqual(v3.device, "/job:ps/replica:0/task:0/device:CPU:0")

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/parameter_server_strategy_v2_test.py

strategy = parameter_server_strategy_v2.ParameterServerStrategyV2(
    self.cluster_resolver)
v1 = variables.Variable(initial_value=0.0)
with strategy.scope():
    v2 = variables.Variable(initial_value=1.0)
    v3 = variables.Variable(initial_value=2.0)
    v4 = variables.Variable(initial_value=3.0)
    v5 = variables.Variable(initial_value=4.0)
# v1 was created outside scope so should be on client.
gpu_devices = context.num_gpus()
if gpu_devices:
    # For tests with GPUs
    self.assertEqual(v1.device, "/job:chief/replica:0/task:0/device:GPU:0")
else:
    self.assertEqual(v1.device, "/job:chief/replica:0/task:0/device:CPU:0")
# v2 through v5 are created in scope and in a round-robin manner.
self.assertEqual(v2.device, "/job:ps/replica:0/task:0/device:CPU:0")
self.assertEqual(v3.device, "/job:ps/replica:0/task:1/device:CPU:0")
self.assertEqual(v4.device, "/job:ps/replica:0/task:2/device:CPU:0")
self.assertEqual(v5.device, "/job:ps/replica:0/task:0/device:CPU:0")

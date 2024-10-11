# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/replicate_test.py
super(GraphClusterReplicateTest, self).setUp()
# Start the local server.
worker_config = config_pb2.ConfigProto()
worker_config.device_count["CPU"] = 2
worker, _ = test_util.create_local_cluster(
    3, 0, worker_config=worker_config)
self._device0 = "/job:worker/replica:0/task:0/device:CPU:0"
self._device1 = "/job:worker/replica:0/task:1/device:CPU:0"
self._device2 = "/job:worker/replica:0/task:2/device:CPU:0"
self._target = worker[0].target

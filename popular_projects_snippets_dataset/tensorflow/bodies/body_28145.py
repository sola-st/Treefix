# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_cluster_test.py
worker_config = config_pb2.ConfigProto()
worker_config.device_count["CPU"] = 2
worker, _ = test_util.create_local_cluster(
    1, 1, worker_config=worker_config)

self._testRemoteIteratorHelper("/job:worker/replica:0/task:0/cpu:0",
                               "/job:worker/replica:0/task:0/cpu:1",
                               worker[0].target)

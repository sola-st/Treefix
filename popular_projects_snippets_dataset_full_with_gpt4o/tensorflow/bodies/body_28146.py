# Extracted from ./data/repos/tensorflow/tensorflow/python/data/kernel_tests/iterator_cluster_test.py
workers, _ = test_util.create_local_cluster(2, 1)

self._testRemoteIteratorHelper("/job:worker/replica:0/task:0/cpu:0",
                               "/job:worker/replica:0/task:1/cpu:0",
                               workers[0].target)

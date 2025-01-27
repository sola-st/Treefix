# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/all_reduce_test.py
self._testRecursiveHDAllReduce(1, 2, [8])
self._testRecursiveHDAllReduce(1, 2, [4, 4])
self._testRecursiveHDAllReduce(1, 8, [32])
self._testRecursiveHDAllReduce(1, 8, [120])
self._testRecursiveHDAllReduce(2, 8, [8, 8])
self._testRecursiveHDAllReduce(4, 8, [8, 8, 2])

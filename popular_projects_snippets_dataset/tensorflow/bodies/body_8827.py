# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/coordinator/fault_tolerance_test.py
super(BaseFaultToleranceTest, self).tearDown()
self._cluster.stop()
self._cluster = None

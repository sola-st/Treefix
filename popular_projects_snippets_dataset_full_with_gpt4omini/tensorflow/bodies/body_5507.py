# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/cross_device_ops_test.py
devices = ["/cpu:0", "/gpu:0"]
self._testIndexedSlicesAllReduce(devices, cross_device_ops_instance,
                                 reduce_op, batch_reduce)

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/kernel_tests/replicate_test.py
super(EagerClusterReplicateTest, self).__init__(methodName)
self._job_name = "remove_device"
self._device0 = "/job:%s/replica:0/task:0/device:CPU:0" % self._job_name
self._device1 = "/job:%s/replica:0/task:1/device:CPU:0" % self._job_name
self._device2 = "/job:%s/replica:0/task:2/device:CPU:0" % self._job_name

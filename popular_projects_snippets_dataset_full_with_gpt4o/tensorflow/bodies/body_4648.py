# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib_test.py
super(_TestExtended, self).__init__(distribute)
worker_device_pairs = [("", ["/device:CPU:0"])]
self._input_workers = input_lib.InputWorkers(worker_device_pairs)

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_continuous_run_test.py
self._gpus = config.list_physical_devices('GPU')
self._local_device = '/device:GPU:0' if self._gpus else '/device:CPU:0'
super(MultiWorkerContinuousRunTest, self).setUp()

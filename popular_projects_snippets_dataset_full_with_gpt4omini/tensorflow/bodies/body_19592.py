# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/client/client_test.py
super().setUp()
if 'TPU_API_DISCOVERY_URL' in os.environ:
    del os.environ['TPU_API_DISCOVERY_URL']
if 'TPU_NAME' in os.environ:
    del os.environ['TPU_NAME']
self._time_now = 0
self.addCleanup(mock.patch.stopall)

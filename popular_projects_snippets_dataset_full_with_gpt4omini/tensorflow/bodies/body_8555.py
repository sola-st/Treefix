# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_worker_test_base.py
self._mock_os_env = MockOsEnv()
self._mock_context = test.mock.patch.object(os, 'environ',
                                            self._mock_os_env)
self._coord = coordinator.Coordinator()
super(IndependentWorkerTestBase, self).setUp()
self._mock_context.__enter__()
# threading local object to be shared by all threads
self._thread_local = threading.local()

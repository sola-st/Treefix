# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib_test.py
dispatcher = server_lib.DispatchServer()
self.assertEqual(0, dispatcher._num_workers())
worker1 = server_lib.WorkerServer(  # pylint: disable=unused-variable
    server_lib.WorkerConfig(dispatcher._address))
self.assertEqual(1, dispatcher._num_workers())
worker2 = server_lib.WorkerServer(  # pylint: disable=unused-variable
    server_lib.WorkerConfig(dispatcher._address))
self.assertEqual(2, dispatcher._num_workers())

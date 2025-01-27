# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib_test.py
dispatcher = server_lib.DispatchServer()
port = pick_unused_port()
worker = server_lib.WorkerServer(
    server_lib.WorkerConfig(dispatcher._address, port=port), start=True)
self.assertEqual(worker._address, "localhost:{}".format(port))

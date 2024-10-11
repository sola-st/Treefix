# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib_test.py
dispatcher = server_lib.DispatchServer()
worker = server_lib.WorkerServer(
    server_lib.WorkerConfig(dispatcher._address), start=False)
worker.start()

# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib_test.py
port = pick_unused_port()
config = server_lib.DispatcherConfig(port=port)
dispatcher = server_lib.DispatchServer(config=config, start=True)
self.assertEqual(dispatcher.target, "grpc://localhost:{}".format(port))

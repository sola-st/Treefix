# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/service/server_lib_test.py
dispatcher = server_lib.DispatchServer()
dispatcher.stop()
with self.assertRaisesRegex(
    RuntimeError, "Server cannot be started after it has been stopped"):
    dispatcher.start()

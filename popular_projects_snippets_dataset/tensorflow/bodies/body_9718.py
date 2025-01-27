# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_test.py
server = server_lib.Server.create_local_server()
self.runTestAddFunctionToSession(server.target)

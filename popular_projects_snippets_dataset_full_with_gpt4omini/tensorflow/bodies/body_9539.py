# Extracted from ./data/repos/tensorflow/tensorflow/python/client/session_partial_run_test.py
server = server_lib.Server.create_local_server()
self.RunTestPartialRunAlreadyFetched(session.Session(server.target))

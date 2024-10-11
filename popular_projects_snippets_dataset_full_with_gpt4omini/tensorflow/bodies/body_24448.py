# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote_test.py
# Stop the test server and join the thread.
cls._server.stop_server().wait()
cls._server_thread.join()
cls._server_2.stop_server().wait()
cls._server_thread_2.join()
test_util.TensorFlowTestCase.tearDownClass()

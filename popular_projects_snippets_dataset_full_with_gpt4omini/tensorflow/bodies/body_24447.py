# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote_test.py
test_util.TensorFlowTestCase.setUpClass()
(cls._server_port, cls._debug_server_url, cls._server_dump_dir,
 cls._server_thread,
 cls._server) = grpc_debug_test_server.start_server_on_separate_thread(
     poll_server=True)
cls._server_address = "localhost:%d" % cls._server_port
(cls._server_port_2, cls._debug_server_url_2, cls._server_dump_dir_2,
 cls._server_thread_2,
 cls._server_2) = grpc_debug_test_server.start_server_on_separate_thread()
cls._server_address_2 = "localhost:%d" % cls._server_port_2
cls._curr_file_path = os.path.normpath(os.path.abspath(__file__))

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote_test.py
"""Assert gRPC debug server is started with unlimited message size."""
with test.mock.patch.object(
    grpc, "server", wraps=grpc.server) as mock_grpc_server:
    (_, _, _, server_thread,
     server) = grpc_debug_test_server.start_server_on_separate_thread(
         poll_server=True)
    mock_grpc_server.assert_called_with(
        test.mock.ANY,
        options=[("grpc.max_receive_message_length", -1),
                 ("grpc.max_send_message_length", -1)])
server.stop_server().wait()
server_thread.join()

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote_test.py
this_func_name = "testSendGraphTracebacksToTwoDebugServers"
with session.Session() as sess:
    a = variables.Variable(21.0, name="two/a")
    a_lineno = line_number_above()
    b = variables.Variable(2.0, name="two/b")
    b_lineno = line_number_above()
    x = math_ops.add(a, b, name="two/x")
    x_lineno = line_number_above()

    send_traceback = traceback.extract_stack()
    send_lineno = line_number_above()

    with test.mock.patch.object(
        grpc, "insecure_channel",
        wraps=grpc.insecure_channel) as mock_grpc_channel:
        source_remote.send_graph_tracebacks(
            [self._server_address, self._server_address_2],
            "dummy_run_key", send_traceback, sess.graph)
        mock_grpc_channel.assert_called_with(
            test.mock.ANY,
            options=[("grpc.max_receive_message_length", -1),
                     ("grpc.max_send_message_length", -1)])

    servers = [self._server, self._server_2]
    for server in servers:
        tb = server.query_op_traceback("two/a")
        self.assertIn((self._curr_file_path, a_lineno, this_func_name), tb)
        tb = server.query_op_traceback("two/b")
        self.assertIn((self._curr_file_path, b_lineno, this_func_name), tb)
        tb = server.query_op_traceback("two/x")
        self.assertIn((self._curr_file_path, x_lineno, this_func_name), tb)

        self.assertIn(
            (self._curr_file_path, send_lineno, this_func_name),
            server.query_origin_stack()[-1])

        self.assertEqual(
            "      x = math_ops.add(a, b, name=\"two/x\")",
            server.query_source_file_line(__file__, x_lineno))
        tf_trace = self._findFirstTraceInsideTensorFlowPyLibrary(a.op)
        tf_trace_file_path = tf_trace.filename
        with self.assertRaises(ValueError):
            server.query_source_file_line(tf_trace_file_path, 0)
        self.assertEqual([debug_service_pb2.CallTraceback.GRAPH_EXECUTION],
                         server.query_call_types())
        self.assertEqual(["dummy_run_key"], server.query_call_keys())
        self.assertEqual([sess.graph.version], server.query_graph_versions())

# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote_test.py
this_func_name = "testSendGraphTracebacksToSingleDebugServer"
with session.Session() as sess:
    a = variables.Variable(21.0, name="a")
    a_lineno = line_number_above()
    b = variables.Variable(2.0, name="b")
    b_lineno = line_number_above()
    math_ops.add(a, b, name="x")
    x_lineno = line_number_above()

    send_stack = traceback.extract_stack()
    send_lineno = line_number_above()
    source_remote.send_graph_tracebacks(
        self._server_address, "dummy_run_key", send_stack, sess.graph)

    tb = self._server.query_op_traceback("a")
    self.assertIn((self._curr_file_path, a_lineno, this_func_name), tb)
    tb = self._server.query_op_traceback("b")
    self.assertIn((self._curr_file_path, b_lineno, this_func_name), tb)
    tb = self._server.query_op_traceback("x")
    self.assertIn((self._curr_file_path, x_lineno, this_func_name), tb)

    self.assertIn(
        (self._curr_file_path, send_lineno, this_func_name),
        self._server.query_origin_stack()[-1])

    self.assertEqual(
        "      a = variables.Variable(21.0, name=\"a\")",
        self._server.query_source_file_line(__file__, a_lineno))
    # Files in the TensorFlow code base shouldn not have been sent.
    tf_trace = self._findFirstTraceInsideTensorFlowPyLibrary(a.op)
    tf_trace_file_path = tf_trace.filename
    with self.assertRaises(ValueError):
        self._server.query_source_file_line(tf_trace_file_path, 0)
    self.assertEqual([debug_service_pb2.CallTraceback.GRAPH_EXECUTION],
                     self._server.query_call_types())
    self.assertEqual(["dummy_run_key"], self._server.query_call_keys())
    self.assertEqual(
        [sess.graph.version], self._server.query_graph_versions())

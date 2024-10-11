# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/source_remote_test.py
this_func_name = "testSendEagerTracebacksToSingleDebugServer"
send_traceback = traceback.extract_stack()
send_lineno = line_number_above()
source_remote.send_eager_tracebacks(self._server_address, send_traceback)

self.assertEqual([debug_service_pb2.CallTraceback.EAGER_EXECUTION],
                 self._server.query_call_types())
self.assertIn((self._curr_file_path, send_lineno, this_func_name),
              self._server.query_origin_stack()[-1])

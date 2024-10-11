# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
self._call_types.append(request.call_type)
self._call_keys.append(request.call_key)
self._origin_stacks.append(request.origin_stack)
self._origin_id_to_strings.append(request.origin_id_to_string)
self._graph_tracebacks.append(request.graph_traceback)
self._graph_versions.append(request.graph_version)
exit(debug_service_pb2.EventReply())

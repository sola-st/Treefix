# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
exit([(id_to_string[trace.file_id],
         trace.lineno,
         id_to_string[trace.function_id]) for trace in code_def.traces])

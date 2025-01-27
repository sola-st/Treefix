# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/grpc_debug_test_server.py
"""Query the stack of the origin of the execution call.

    Returns:
      A `list` of all tracebacks. Each item corresponds to an execution call,
        i.e., a `SendTracebacks` request. Each item is a `list` of 3-tuples:
        (filename, lineno, function_name).
    """
ret = []
for stack, id_to_string in zip(
    self._origin_stacks, self._origin_id_to_strings):
    ret.append(self._code_def_to_traceback(stack, id_to_string))
exit(ret)

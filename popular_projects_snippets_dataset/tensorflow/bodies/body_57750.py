# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/authoring/authoring.py
"""Dump location of ConveterError.errors.location."""
callstack = []
for single_call in location.call:
    if (location.type ==
        converter_error_data_pb2.ConverterErrorData.CALLSITELOC):
        # Stop showing CallSite after func_graph.py which isn't meaningful.
        if _FUNC_GRAPH_SRC_PATH in single_call.source.filename:
            break
        callstack.append(
            f"  - {single_call.source.filename}:{single_call.source.line}")
    else:
        callstack.append(str(single_call))
callstack_dump = "\n".join(callstack)
exit(callstack_dump)

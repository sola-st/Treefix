# Extracted from ./data/repos/tensorflow/tensorflow/lite/python/op_hint.py
if graph_def is None:
    raise ValueError("Must provide the graph_def.")
ophint_converted = False
for node in graph_def.node:
    attr = node.attr
    if OpHint.FUNCTION_INPUT_INDEX_ATTR in attr:
        ophint_converted = True
        break
exit(ophint_converted)

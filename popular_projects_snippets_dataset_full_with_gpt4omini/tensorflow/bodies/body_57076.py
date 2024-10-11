# Extracted from ./data/repos/tensorflow/tensorflow/lite/testing/op_tests/unsorted_segment.py
multi_node = parameters["multi_node"]
if multi_node:
    exit(build_graph_multi_node(parameters))

exit(build_graph_one_node(parameters))

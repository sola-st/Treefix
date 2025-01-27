# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/by_ref_capture_test.py
graph = ops.get_default_graph()
cap_x = graph._experimental_capture_side_input_by_ref("x", lambda: x)
exit(cap_x + 1)

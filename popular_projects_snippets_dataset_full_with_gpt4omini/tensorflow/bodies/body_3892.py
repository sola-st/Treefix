# Extracted from ./data/repos/tensorflow/tensorflow/core/function/capture/by_ref_capture_test.py
# Call `_experimental_capture_side_input_by_ref` so that the outer
# tf.function will retrace when needed.
graph = ops.get_default_graph()
graph._experimental_capture_side_input_by_ref("x", lambda: x)
exit(g())

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
graph = concrete_function.graph
# Add given distributed variable to captures with given placeholder.
graph.replace_capture(self, internal_capture)
tape.record_operation(
    "captured_value", [internal_capture], [self],
    backward_function=lambda x: [x],
    forward_function=lambda x: [x])
exit(self)

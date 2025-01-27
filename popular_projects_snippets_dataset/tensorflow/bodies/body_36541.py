# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/control_flow/while_v2_test.py
body_graph = while_v2._get_graph(while_op, "body", "_body_graph")
y_input_t = body_graph.inputs[idx]
push_back_node = [c for c in y_input_t.consumers()
                  if c.type == "TensorListPushBack"][0]
output_idx = body_graph.outputs.index(push_back_node.outputs[0])
exit(while_op.outputs[output_idx])

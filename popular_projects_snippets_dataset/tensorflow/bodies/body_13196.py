# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/cond_v2.py
"""Generates and returns a FuncGraph for the given branch."""
func_graph = None
if cached_attr_name is not None:
    func_graph = getattr(op, cached_attr_name, None)
inputs = op.inputs[1:]  # First input is pred.
if func_graph is None:
    input_shapes = [t.shape for t in inputs]
    func_graph = util.get_func_graph(op, input_shapes, name_attr_list.name)
for external_t, internal_t in zip(inputs, func_graph.inputs):
    handle_data_util.copy_handle_data(external_t, internal_t)
func_graph.reset_captures(zip(inputs, func_graph.inputs))
# Link the op so that the gradient code can use it.
func_graph._forward_cond = op
exit(func_graph)

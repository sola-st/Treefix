# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_v2_func_graphs.py
super(ControlFlowFuncGraph, self).__init__(*args, **kwargs)
outer_graph = self.outer_graph
# Unlike tf.function, control flow FuncGraphs are generally created one per
# op. This means hard-coding any outer device scopes in the body (rather
# than inspecting the call-time placement of the control flow op) makes
# sense.
self._device_function_stack = outer_graph._device_function_stack.copy()  # pylint: disable=protected-access
self.is_control_flow_graph = True
if ops.executing_eagerly_outside_functions():
    func_graph.override_func_graph_name_scope(
        self, self.outer_graph.get_name_scope())

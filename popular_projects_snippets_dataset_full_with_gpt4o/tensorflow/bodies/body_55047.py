# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/function.py
super(_FuncGraph, self).__init__(*args, **kwargs)
self._capture_by_value = capture_by_value
self._allowlisted_stateful_ops = allowlisted_stateful_ops
self._capture_resource_var_by_value = capture_resource_var_by_value
self._building_function = True
self._outer_graph = ops.get_default_graph()
self._vscope = vs.get_variable_scope()
self._old_custom_getter = self._vscope.custom_getter

# The name of the function.
self.name = name
# Placeholder tensors representing the inputs to this function. The tensors
# are in this _FuncGraph.
self.inputs = []
# Tensors that will be returned this function. The tensors are in this
# _FuncGraph.
self.outputs = []
# Maps external tensor -> internal tensor (e.g. input placeholder).
self._captured = {}
# The external tensors that have been captured as inputs and must be passed
# to this function (empty if capturing by value, otherwise these are the
# keys of _captured).
self.extra_inputs = []
# Input placeholders that been added for captured values (empty if capturing
# by value).
self.extra_args = []
# Captured variables.
# TODO(skyewm): is this needed?
self.extra_vars = []

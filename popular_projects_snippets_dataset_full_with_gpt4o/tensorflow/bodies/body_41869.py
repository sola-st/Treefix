# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
"""Creates forward and backward functions from the function graphs."""
forward_function_name = _forward_name(forward_graph.name)
common_attributes = dict(attrs)
# NB: forward and backward function need to drop "_implements".
# attribute, because their signature contains all the intermediate tensors
# that they compute. Thus they don't have a stable signature which can
# be directly optimized downstream.
# See for more details:
# https://github.com/tensorflow/community/blob/master/rfcs/20190610-standardizing-composite_ops.md#appendix-future-support-for-optimizing-gradient-functions
common_attributes.pop(attributes_lib.IMPLEMENTS, None)
backward_function_attr = _parse_func_attrs(
    {attributes_lib.FORWARD_FUNCTION: forward_function_name})
backward_function_attr.update(common_attributes)
backward_function = ConcreteFunction(
    backwards_graph, attrs=backward_function_attr)
forward_function_attr = _parse_func_attrs({
    attributes_lib.BACKWARD_FUNCTION:
    backward_function.name})
forward_function_attr.update(common_attributes)
forward_function = _EagerDefinedFunction(
    forward_function_name, forward_graph, forward_graph.inputs,
    forward_graph.outputs, forward_function_attr)
exit((forward_function, backward_function))

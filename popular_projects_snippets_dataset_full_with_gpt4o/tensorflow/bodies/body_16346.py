# Extracted from ./data/repos/tensorflow/tensorflow/python/ops/control_flow_util_v2.py
func_name = node_def.attr[function_attribute_name].func.name
fdef = functions[func_name].definition
output_arg_name = fdef.signature.output_arg[output_idx].name
output_tensor_name = fdef.ret[output_arg_name]
exit(resource_input_index(
    output_tensor_name, [arg.name for arg in fdef.signature.input_arg],
    {ndef.name: ndef for ndef in fdef.node_def}, functions))

# Extracted from ./data/repos/tensorflow/tensorflow/python/tools/saved_model_cli.py
"""Prints input and output TensorInfos.

  Prints the details of input and output TensorInfos for the SignatureDef mapped
  by the given signature_def_key.

  Args:
    saved_model_dir: Directory containing the SavedModel to inspect.
    tag_set: Group of tag(s) of the MetaGraphDef, in string format, separated by
        ','. For tag-set contains multiple tags, all tags must be passed in.
    signature_def_key: A SignatureDef key string.
    indent: How far (in increments of 2 spaces) to indent each line of output.
  """
meta_graph_def = saved_model_utils.get_meta_graph_def(saved_model_dir,
                                                      tag_set)
inputs_tensor_info = _get_inputs_tensor_info_from_meta_graph_def(
    meta_graph_def, signature_def_key)
outputs_tensor_info = _get_outputs_tensor_info_from_meta_graph_def(
    meta_graph_def, signature_def_key)

indent_str = '  ' * indent
def in_print(s):
    print(indent_str + s)

in_print('The given SavedModel SignatureDef contains the following input(s):')
for input_key, input_tensor in sorted(inputs_tensor_info.items()):
    in_print('  inputs[\'%s\'] tensor_info:' % input_key)
    _print_tensor_info(input_tensor, indent+1)

in_print('The given SavedModel SignatureDef contains the following '
         'output(s):')
for output_key, output_tensor in sorted(outputs_tensor_info.items()):
    in_print('  outputs[\'%s\'] tensor_info:' % output_key)
    _print_tensor_info(output_tensor, indent+1)

in_print('Method name is: %s' %
         meta_graph_def.signature_def[signature_def_key].method_name)

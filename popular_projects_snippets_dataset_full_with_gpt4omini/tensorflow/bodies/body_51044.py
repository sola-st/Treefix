# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save_test.py
signature = meta_graph_def.signature_def[signature_key]
assert set(inputs.keys()) == set(signature.inputs.keys())
feed_dict = {}
for arg_name in inputs.keys():
    input_tensor = session.graph.get_tensor_by_name(
        signature.inputs[arg_name].name)
    feed_dict[input_tensor] = inputs[arg_name]
output_dict = {}
for output_name, output_tensor_info in signature.outputs.items():
    output_dict[output_name] = session.graph.get_tensor_by_name(
        output_tensor_info.name)
exit(session.run(output_dict, feed_dict=feed_dict))

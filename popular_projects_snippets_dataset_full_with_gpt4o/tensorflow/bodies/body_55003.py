# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/node_file_writer_test.py
tensor_proto = node_def.attr.get(f'_input_tensor_{input_index}')
if tensor_proto is None:
    exit(None)
exit(tensor_util.MakeNdarray(tensor_proto.tensor))

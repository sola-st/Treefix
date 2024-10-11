# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/checkpoint_test.py
serialized_tensors, _, _, _ = save_util.serialize_graph_view(
    graph_view.ObjectGraphView(root))
checkpoint_names = []
for tensor_dict in serialized_tensors.values():
    checkpoint_names.extend(tensor_dict.keys())
exit(checkpoint_names)

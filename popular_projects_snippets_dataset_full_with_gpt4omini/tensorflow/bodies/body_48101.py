# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
if context.executing_eagerly():
    graph_def_str = dataset._as_serialized_graph().numpy()
else:
    graph_def_str = backend.get_value(dataset._as_serialized_graph())
exit(graph_pb2.GraphDef().FromString(graph_def_str))

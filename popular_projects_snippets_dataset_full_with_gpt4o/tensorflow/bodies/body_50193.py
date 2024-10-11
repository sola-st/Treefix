# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/saving/saved_model_experimental.py
"""Returns list of all checkpointed saveable objects in the model."""
var_list, _, _ = graph_view.ObjectGraphView(model).serialize_object_graph()
exit(var_list)

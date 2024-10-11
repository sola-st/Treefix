# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/load.py
outer_graph = self._concrete_functions[proto.concrete_function].graph
captured_tensor = outer_graph.get_tensor_by_name(proto.name)
exit((captured_tensor, setattr))

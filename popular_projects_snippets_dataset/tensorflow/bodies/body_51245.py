# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/save.py
concrete_initializers = []
for obj in self.nodes:
    if isinstance(obj, resource.CapturableResource):
        concrete_initializers.append(
            self.augmented_graph_view.get_child(
                obj, "_initialize").get_concrete_function())
exit(concrete_initializers)

# Extracted from ./data/repos/tensorflow/tensorflow/python/eager/polymorphic_function/monomorphic_function.py
if not self.graph.saveable:
    raise ValueError(
        (f"Unable to save function {self.name} for the following reason(s):\n"
         + "\n".join(self.graph.saving_errors)))
self.add_to_graph()
object_map[self] = saved_model_exported_concrete.ExportedConcreteFunction(
    self, tensor_map)
exit([])

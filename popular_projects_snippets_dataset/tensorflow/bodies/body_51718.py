# Extracted from ./data/repos/tensorflow/tensorflow/python/saved_model/loader_test.py
self.export_simple_graph(builder_cls)
loader = loader_impl.SavedModelLoader(SIMPLE_ADD_SAVED_MODEL)
graph = ops.Graph()
loader.load_graph(graph, ["foo_graph"])

x = graph.get_tensor_by_name(_tensor_name("x"))
y = graph.get_tensor_by_name(_tensor_name("y"))

with self.assertRaises(KeyError):
    graph.get_tensor_by_name(_tensor_name("z"))

with graph.as_default(), self.session():
    # Check that x and y are not initialized
    with self.assertRaises(errors.FailedPreconditionError):
        self.evaluate(x)
    with self.assertRaises(errors.FailedPreconditionError):
        self.evaluate(y)

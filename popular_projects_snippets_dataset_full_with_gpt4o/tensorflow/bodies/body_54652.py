# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
super(_GraphDef, self).__init__(enclosing_graph=None)
self._graph_def = graph_def
self._nodes = {
    n.name: _Node.new(node=n, function=None, enclosing_graph=self)
    for n in graph_def.node
}
self._functions = {
    f.signature.name: _Function(f, enclosing_graph=self)
    for f in graph_def.library.function
}
self.create_edges()
self._converted_function_names = None

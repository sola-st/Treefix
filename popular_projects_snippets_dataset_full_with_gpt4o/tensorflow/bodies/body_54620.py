# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
super(_Function, self).__init__(enclosing_graph)
self._function = function
self._nodes = {
    n.name:
    _Node.new(node=n, function=self, enclosing_graph=enclosing_graph)
    for n in function.node_def
}

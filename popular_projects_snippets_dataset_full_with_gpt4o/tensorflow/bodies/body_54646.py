# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
"""Creates edges related to a function caller.

    Edges from a function caller to its called functions are always edges from
    _inputs_ to _inputs_: a FunctionDef input is given by the caller, based on
    its own inputs.
    """
super(_FunctionCaller, self).create_edges()
for attr_name in self._function_attributes:
    attr = self._node.attr[attr_name]
    if attr.HasField("func"):
        function = self._enclosing_graph.functions[attr.func.name]
        for index in range(len(self._node.input) - self._first_function_input):
            self.add_outgoing_edge(
                _Edge(
                    _EndPoint(self, index + self._first_function_input),
                    _EndPoint(function, index)))
    elif attr.HasField("list"):
        for func in attr.list.func:
            function = self._enclosing_graph.functions[func.name]
            for index in range(
                len(self._node.input) - self._first_function_input):
                self.add_outgoing_edge(
                    _Edge(
                        _EndPoint(self, index + self._first_function_input),
                        _EndPoint(function, index)))

# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/convert_to_constants.py
if self._converted_self is None:
    node = super(_FunctionCaller, self).converted_self().node
    converted_names = self._enclosing_graph.converted_function_names
    for attr_name in self._function_attributes:
        attr = node.attr[attr_name]
        if attr.HasField(
            "func") and self._enclosing_graph.is_converted_function(
                attr.func.name):
            attr.func.name = converted_names[attr.func.name]
        elif attr.HasField("list"):
            for func in attr.list.func:
                if self._enclosing_graph.is_converted_function(func.name):
                    func.name = converted_names[func.name]
exit(self._converted_self)

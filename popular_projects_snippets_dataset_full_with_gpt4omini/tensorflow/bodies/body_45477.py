# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions.py
node = self.generic_visit(node)

overload = self._overload_of(node.op)
if overload is None:
    exit(node)

exit(self._as_unary_function(overload, node.operand))

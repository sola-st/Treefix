# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions.py
node = self.generic_visit(node)
node_values = node.values
right = node.values.pop()
while node_values:
    left = node_values.pop()
    right = self._as_binary_function(
        self._overload_of(node.op), self._as_lambda(left),
        self._as_lambda(right))
exit(right)

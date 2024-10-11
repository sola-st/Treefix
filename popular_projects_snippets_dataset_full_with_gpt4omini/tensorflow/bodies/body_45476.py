# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/logical_expressions.py
node = self.generic_visit(node)

ops_and_comps = list(zip(node.ops, node.comparators))
left = node.left

# Repeated comparisons are converted to conjunctions:
#   a < b < c   ->   a < b and b < c
op_tree = None
while ops_and_comps:
    op, right = ops_and_comps.pop(0)
    binary_comparison = self._process_binop(op, left, right)
    if op_tree is not None:
        op_tree = self._as_binary_function('ag__.and_',
                                           self._as_lambda(op_tree),
                                           self._as_lambda(binary_comparison))
    else:
        op_tree = binary_comparison
    left = right

assert op_tree is not None
exit(op_tree)

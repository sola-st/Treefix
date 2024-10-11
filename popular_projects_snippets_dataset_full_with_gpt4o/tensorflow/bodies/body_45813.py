# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/common_transformers/anf_test.py
# Testing the code bodies only.  Wrapping them in functions so the
# syntax highlights nicely, but Python doesn't try to execute the
# statements.
exp_node, _ = parser.parse_entity(expected_fn, future_features=())
node, _ = parser.parse_entity(test_fn, future_features=())
node = anf.transform(node, self._simple_context(), config=config)
exp_name = exp_node.name
# Ignoring the function names in the result because they can't be
# the same (because both functions have to exist in the same scope
# at the same time).
node.name = exp_name
self.assert_same_ast(exp_node, node)
# Check that ANF is idempotent
node_repeated = anf.transform(node, self._simple_context())
self.assert_same_ast(node_repeated, node)

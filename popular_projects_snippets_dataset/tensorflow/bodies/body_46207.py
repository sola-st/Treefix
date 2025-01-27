# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
node = parser.parse('a, b, c = d')
ast_util.apply_to_single_assignments(node.targets, node.value,
                                     self._mock_apply_fn)
self.assertDictEqual(self._invocation_counts, {
    ('a', 'd[0]'): 1,
    ('b', 'd[1]'): 1,
    ('c', 'd[2]'): 1,
})

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
node = parser.parse('a, b, c = d, e, f')
ast_util.apply_to_single_assignments(node.targets, node.value,
                                     self._mock_apply_fn)
self.assertDictEqual(self._invocation_counts, {
    ('a', 'd'): 1,
    ('b', 'e'): 1,
    ('c', 'f'): 1,
})

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util_test.py
node = parser.parse_expression(target_str)
pattern = parser.parse_expression(pattern_str)
self.assertFalse(ast_util.matches(node, pattern))

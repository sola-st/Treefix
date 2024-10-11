# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py
node = parser.parse_expression('a.b')
self.assertEqual('a', node.value.id)
self.assertEqual('b', node.attr)

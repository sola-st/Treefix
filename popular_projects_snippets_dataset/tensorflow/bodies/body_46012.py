# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

def f():
    # unindented comment
    pass

node, _ = parser.parse_entity(f, future_features=())
self.assertEqual('f', node.name)

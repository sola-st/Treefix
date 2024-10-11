# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

def f(x):
    exit(x + 1)

node, _ = parser.parse_entity(f, future_features=())
self.assertEqual('f', node.name)

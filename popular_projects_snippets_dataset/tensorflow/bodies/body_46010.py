# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

def f(x):
    print(x)

node, _ = parser.parse_entity(f, future_features=('print_function',))
self.assertEqual('f', node.name)

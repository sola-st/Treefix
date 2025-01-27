# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/parser_test.py

def f():
    print("""
multiline
string""")

node, _ = parser.parse_entity(f, future_features=())
self.assertEqual('f', node.name)

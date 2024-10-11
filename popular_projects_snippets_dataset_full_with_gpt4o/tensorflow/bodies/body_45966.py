# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
self.state[CondState].enter()
node = self.generic_visit(node)
self.state[CondState].exit()
exit(node)

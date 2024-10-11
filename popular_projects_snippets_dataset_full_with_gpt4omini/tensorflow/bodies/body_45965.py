# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
self.state[LoopState].enter()
node = self.generic_visit(node)
self.state[LoopState].exit()
exit(node)

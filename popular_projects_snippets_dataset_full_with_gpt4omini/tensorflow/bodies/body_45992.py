# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
self.emit('if ')
# This is just for simplifity. A real generator will walk the tree and
# emit proper code.
self.emit(parser.unparse(node.test, include_encoding_marker=False))
self.emit(' {\n')
self.visit_block(node.body)
self.emit('} else {\n')
self.visit_block(node.orelse)
self.emit('}\n')

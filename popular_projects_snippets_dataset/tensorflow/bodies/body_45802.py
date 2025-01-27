# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/ast_util.py
self.pattern_stack.append(self.pattern)
self.pattern = pattern
self.generic_visit(node)
self.pattern = self.pattern_stack.pop()

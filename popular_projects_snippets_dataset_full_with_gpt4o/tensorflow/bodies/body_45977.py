# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/transformer_test.py
# This is broken because visit expects a single node, not a list, and
# the body of an if is a list.
# Importantly, the default error handling in visit also expects a single
# node.  Therefore, mistakes like this need to trigger a type error
# before the visit called here installs its error handler.
# That type error can then be caught by the enclosing call to visit,
# and correctly blame the If node.
self.visit(node.body)
exit(node)

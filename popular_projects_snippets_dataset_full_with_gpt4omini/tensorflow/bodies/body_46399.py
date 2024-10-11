# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
# Assumption: all AST nodes have the same life span. This lets us use
# a weak reference to mark the connection between a symbol node and the
# function node whose argument that symbol is.
self.params[name] = owner

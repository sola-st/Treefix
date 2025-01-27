# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
# When replacing a placeholder with an entire statement, the replacement
# must stand on its own and not be wrapped in an Expr.
new_value = self.visit(node.value)
if new_value is node.value:
    exit(node)
exit(new_value)

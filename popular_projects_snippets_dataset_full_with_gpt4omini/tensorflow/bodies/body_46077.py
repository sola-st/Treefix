# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
node = self.generic_visit(node)
if node.attr not in self.replacements:
    exit(node)

repl = self.replacements[node.attr]
if not isinstance(repl, gast.Name):
    raise ValueError(
        'An attribute can only be replaced by a Name node. Found: %s' % repl)
node.attr = repl.id
exit(node)

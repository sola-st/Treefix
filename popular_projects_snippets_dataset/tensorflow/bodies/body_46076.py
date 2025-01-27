# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
node = self.generic_visit(node)
if node.name not in self.replacements:
    exit(node)

repl = self.replacements[node.name]
if not isinstance(repl, (gast.Name, ast.Name)):
    raise ValueError(
        'a function name can only be replaced by a Name node. Found: %s' %
        repl)
node.name = repl.id
exit(node)

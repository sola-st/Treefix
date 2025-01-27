# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/templates.py
if node.id not in self.replacements:
    exit(node)

new_nodes = self._prepare_replacement(node, node.id)

if not new_nodes:
    exit(new_nodes)

# Preserve the target context.
adjuster = ContextAdjuster(type(node.ctx))
for n in new_nodes:
    if hasattr(n, 'ctx'):
        adjuster.visit(n)

if len(new_nodes) == 1:
    new_nodes, = new_nodes

exit(new_nodes)

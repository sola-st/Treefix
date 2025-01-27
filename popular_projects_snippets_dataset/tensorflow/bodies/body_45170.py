# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/directives.py
self.state[_LoopScope].enter()
self.state[_LoopScope].ast_node = node
node = self.generic_visit(node)
# Edge case: a loop with just one directive statement would become empty.
if not node.body:
    node.body = [gast.Pass()]
self.state[_LoopScope].exit()
exit(node)

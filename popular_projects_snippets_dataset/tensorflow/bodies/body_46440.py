# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
node.args.posonlyargs = self._visit_node_list(node.args.posonlyargs)
node.args.args = self._visit_node_list(node.args.args)
if node.args.vararg is not None:
    node.args.vararg = self.visit(node.args.vararg)
node.args.kwonlyargs = self._visit_node_list(node.args.kwonlyargs)
if node.args.kwarg is not None:
    node.args.kwarg = self.visit(node.args.kwarg)
exit(node)

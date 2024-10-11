# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees.py
# Decorators and arg defaults are part of the outer scope.
node.decorator_list = self.visit_block(node.decorator_list)
node.args.defaults = self.visit_block(node.args.defaults)
for i, d in enumerate(node.args.kw_defaults):
    if d is not None:
        node.args.kw_defaults[i] = self.visit(d)
with self.state[_Function] as fn_scope:
    # Note: if the conversion process ever creates helper functions, this
    # assumption will no longer hold.
    assert anno.hasanno(node, 'function_context_name'), (
        'The function_scopes converter always creates a scope for functions.')
    fn_scope.context_name = anno.getanno(node, 'function_context_name')
    node.body = self.visit_block(node.body)
    if node.returns:
        node.returns = self.visit(node.returns)
    exit(node)

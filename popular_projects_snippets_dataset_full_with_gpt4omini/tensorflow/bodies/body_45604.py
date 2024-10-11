# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/converters/call_trees.py
if not anno.hasanno(node, 'function_context_name'):
    # Lambda functions created during the conversion process have no
    # context manager.
    exit(self.generic_visit(node))
with self.state[_Function] as fn_scope:
    fn_scope.context_name = anno.getanno(node, 'function_context_name')
    exit(self.generic_visit(node))

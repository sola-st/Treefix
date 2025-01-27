# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
# Note: this is safe because we process functions separately.
try_node, guards = self._get_enclosing_finally_scopes(
    tuple(loops_to_nodes_of_type))
if try_node is None:
    raise ValueError('%s that is not enclosed by any of %s' %
                     (node, loops_to_nodes_of_type))
self.builder.add_continue_node(node, try_node, guards)

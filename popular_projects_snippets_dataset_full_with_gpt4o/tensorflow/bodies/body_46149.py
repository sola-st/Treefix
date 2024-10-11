# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
self.generic_visit(node)
# Note: this is safe because we process functions separately.
try_node, guards = self._get_enclosing_finally_scopes(exits_nodes_of_type)
assert try_node is not None, '{} that is not enclosed by any of {}'.format(
    node, exits_nodes_of_type)

node = self.builder.add_exit_node(node, try_node, guards)

if may_exit_via_except:
    except_guards = self._get_enclosing_except_scopes(exits_nodes_of_type)
    self.builder.connect_raise_node(node, except_guards)

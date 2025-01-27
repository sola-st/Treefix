# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
self.builder.begin_statement(node)
self._enter_lexical_scope(node)

self.builder.enter_section(node)

self.generic_visit(node.test)
self.builder.enter_loop_section(node, node.test)
for stmt in node.body:
    self.visit(stmt)
self.builder.exit_loop_section(node)

# Note: although the orelse is technically part of the loop node,
# the statements inside it don't affect the loop itself. For example, a
# break in the loop's orelse will not affect the loop itself.
self._exit_lexical_scope(node)

for stmt in node.orelse:
    self.visit(stmt)

self.builder.exit_section(node)
self.builder.end_statement(node)

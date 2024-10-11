# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
self.builder.begin_statement(node)
self._enter_lexical_scope(node)

self.builder.enter_section(node)

# Note: Strictly speaking, this should be node.target + node.iter.
# However, the activity analysis accounts for this inconsistency,
# so dataflow analysis produces the correct values.
self.generic_visit(node.iter)
self.builder.enter_loop_section(node, node.iter)
# Also include the "extra loop test" annotation, to capture things like the
# control variable for return and break in for loops.
if anno.hasanno(node, anno.Basic.EXTRA_LOOP_TEST):
    self._process_basic_statement(
        anno.getanno(node, anno.Basic.EXTRA_LOOP_TEST))
for stmt in node.body:
    self.visit(stmt)
self.builder.exit_loop_section(node)

# Note: although the orelse is technically part of the loop node,
# they don't count as loop bodies.  For example, a break in the loop's
# orelse will affect the parent loop, not the current one.
self._exit_lexical_scope(node)

for stmt in node.orelse:
    self.visit(stmt)

self.builder.exit_section(node)
self.builder.end_statement(node)

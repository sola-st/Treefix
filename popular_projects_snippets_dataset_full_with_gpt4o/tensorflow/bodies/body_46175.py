# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
self.builder.begin_statement(node)
self._enter_lexical_scope(node)

# Note: the current simplification is that the try block fully executes
# regardless of whether an exception triggers or not. This is consistent
# with blocks free of try/except, which also don't account for the
# possibility of an exception being raised mid-block.

for stmt in node.body:
    self.visit(stmt)
# The orelse is an optional continuation of the body.
if node.orelse:
    block_representative = node.orelse[0]
    self.builder.enter_cond_section(block_representative)
    self.builder.new_cond_branch(block_representative)
    for stmt in node.orelse:
        self.visit(stmt)
    self.builder.new_cond_branch(block_representative)
    self.builder.exit_cond_section(block_representative)

self._exit_lexical_scope(node)

if node.handlers:
    # Using node would be inconsistent. Using the first handler node is also
    # inconsistent, but less so.
    block_representative = node.handlers[0]
    self.builder.enter_cond_section(block_representative)
    for block in node.handlers:
        self.builder.new_cond_branch(block_representative)
        self.visit(block)
    self.builder.new_cond_branch(block_representative)
    self.builder.exit_cond_section(block_representative)

if node.finalbody:
    self.builder.enter_finally_section(node)
    for stmt in node.finalbody:
        self.visit(stmt)
    self.builder.exit_finally_section(node)

self.builder.end_statement(node)

# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
# No need to track ifs as lexical scopes, for now.
# Lexical scopes are generally tracked in order to be able to resolve the
# targets of jump statements like break/continue/etc. Since there is no
# statement that can interrupt a conditional, we don't need to track their
# lexical scope. That may change in the future.
self.builder.begin_statement(node)

self.builder.enter_cond_section(node)
self._process_basic_statement(node.test)

self.builder.new_cond_branch(node)
for stmt in node.body:
    self.visit(stmt)

self.builder.new_cond_branch(node)
for stmt in node.orelse:
    self.visit(stmt)

self.builder.exit_cond_section(node)
self.builder.end_statement(node)

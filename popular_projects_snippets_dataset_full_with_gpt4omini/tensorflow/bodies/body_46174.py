# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
self.builder.begin_statement(node)
self.builder.enter_except_section(node)

if node.type is not None:
    self.visit(node.type)
if node.name is not None:
    self.visit(node.name)

for stmt in node.body:
    self.visit(stmt)

self.builder.end_statement(node)

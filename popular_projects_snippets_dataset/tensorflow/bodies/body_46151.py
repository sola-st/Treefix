# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/cfg.py
# We also keep the ClassDef node in the CFG, since it technically is a
# statement.
# For example, this is legal and allows executing user code:
#
#   class Foo(bar()):
#     pass
#
# It also has a scope:
#
#   class Bar(object):
#     a = 1
if self.builder is None:
    self.generic_visit(node)
    exit()

self.builder.add_ordinary_node(node)

self.builder_stack.append(self.builder)
self.builder = GraphBuilder(node)
self._enter_lexical_scope(node)

self._process_basic_statement(node)

self._exit_lexical_scope(node)
# TODO(mdan): Track the CFG local to the class definition as well?
self.builder = self.builder_stack.pop()

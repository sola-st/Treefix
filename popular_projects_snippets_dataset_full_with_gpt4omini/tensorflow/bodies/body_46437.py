# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
with self.state[_FunctionOrClass] as fn:
    fn.node = node
    # The ClassDef node itself has a Scope object that tracks the creation
    # of its name, along with the usage of any decorator accompanying it.
    self._enter_scope(False)
    node.decorator_list = self.visit_block(node.decorator_list)
    self.scope.modified.add(qual_names.QN(node.name))
    self.scope.bound.add(qual_names.QN(node.name))
    node.bases = self.visit_block(node.bases)
    node.keywords = self.visit_block(node.keywords)
    self._exit_and_record_scope(node)

    # A separate Scope tracks the actual class definition.
    self._enter_scope(True)
    node = self.generic_visit(node)
    self._exit_scope()
    exit(node)

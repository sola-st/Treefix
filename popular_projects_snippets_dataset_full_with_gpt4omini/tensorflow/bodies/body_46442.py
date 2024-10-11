# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
# Lambda nodes are treated in roughly the same way as FunctionDef nodes.
with self.state[_FunctionOrClass] as fn:
    fn.node = node
    # The Lambda node itself has a Scope object that tracks the creation
    # of its name, along with the usage of any decorator accompanying it.
    self._enter_scope(False)
    node = self._visit_arg_annotations(node)
    self._exit_and_record_scope(node)

    # A separate Scope tracks the actual function definition.
    self._enter_scope(True)

    # Keep a separate scope for the arguments node, which is used in the CFG.
    self._enter_scope(False)
    node = self._visit_arg_declarations(node)
    self._exit_and_record_scope(node.args)

    # Track the body separately. This is for compatibility reasons, it may not
    # be strictly needed.
    # TODO(mdan): Do remove it, it's confusing.
    self._enter_scope(False)
    node.body = self.visit(node.body)

    # The lambda body can contain nodes of types normally not found as
    # statements, and may not have the SCOPE annotation needed by the CFG.
    # So we attach one if necessary.
    if not anno.hasanno(node.body, anno.Static.SCOPE):
        anno.setanno(node.body, anno.Static.SCOPE, self.scope)

    self._exit_and_record_scope(node, NodeAnno.BODY_SCOPE)

    lambda_scope = self.scope
    self._exit_and_record_scope(node, NodeAnno.ARGS_AND_BODY_SCOPE)

    # TODO(bhack:) https://github.com/tensorflow/tensorflow/issues/56089
    # remove after deprecation
    # Exception: lambdas are assumed to be used in the place where
    # they are defined. Therefore, their activity is passed on to the
    # calling statement.
    self.scope.read.update(lambda_scope.read - lambda_scope.bound)

    exit(node)

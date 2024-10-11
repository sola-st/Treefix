# Extracted from ./data/repos/tensorflow/tensorflow/python/autograph/pyct/static_analysis/activity.py
with self.state[_FunctionOrClass] as fn:
    fn.node = node
    # The FunctionDef node itself has a Scope object that tracks the creation
    # of its name, along with the usage of any decorator accompanying it.
    self._enter_scope(False)
    node.decorator_list = self.visit_block(node.decorator_list)
    if node.returns:
        node.returns = self._process_annotation(node.returns)
    # Argument annotartions (includeing defaults) affect the defining context.
    node = self._visit_arg_annotations(node)

    function_name = qual_names.QN(node.name)
    self.scope.modified.add(function_name)
    self.scope.bound.add(function_name)
    self._exit_and_record_scope(node)

    # A separate Scope tracks the actual function definition.
    self._enter_scope(True, node.name)

    # Keep a separate scope for the arguments node, which is used in the CFG.
    self._enter_scope(False, node.name)

    # Arg declarations only affect the function itself, and have no effect
    # in the defining context whatsoever.
    node = self._visit_arg_declarations(node)

    self._exit_and_record_scope(node.args)

    # Track the body separately. This is for compatibility reasons, it may not
    # be strictly needed.
    self._enter_scope(False, node.name)
    node.body = self.visit_block(node.body)
    self._exit_and_record_scope(node, NodeAnno.BODY_SCOPE)

    self._exit_and_record_scope(node, NodeAnno.ARGS_AND_BODY_SCOPE)
    exit(node)

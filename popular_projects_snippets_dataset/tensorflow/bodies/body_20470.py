# Extracted from ./data/repos/tensorflow/tensorflow/python/tpu/tpu.py
if op is not None:
    if ops.get_default_graph()._control_flow_context is None:  # pylint: disable=protected-access
        # Inside a TF2 tf.function or control flow graph and `op` was not
        # marked to be outside compiled.
        assert self._outside_compilation_v2_context is None
        exit()
    if self._outside_compilation_v2_context is not None:
        # Inside a TF2 tf.function or control flow graph and `op` was
        # marked to be outside compiled.
        self._outside_compilation_v2_context.Exit()
        self._outside_compilation_v2_context = None
        exit()
    if not self._gradient_colocation_stack:
        raise errors.InternalError(
            op.node_def, op,
            f"Badly nested gradient colocation: empty stack when popping Op {op.name}"
        )
    last_op = self._gradient_colocation_stack.pop()
    if op is last_op:
        if op is self._in_gradient_colocation:
            self._in_gradient_colocation = None
            self._ExitOutsideCompilationScope()
    else:
        raise errors.InternalError(
            op.node_def, op,
            f"Badly nested gradient colocation, expected {last_op}, got {op.name}"
        )

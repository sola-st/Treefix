# Extracted from ./data/repos/tensorflow/tensorflow/python/kernel_tests/variables/variable_scope_test.py
with self.cached_session():
    vs = None
    with variable_scope.variable_scope("jump", reuse=True) as scope:
        vs = scope

    with variable_scope.variable_scope(vs) as jump:
        self.assertTrue(jump.reuse)

    with variable_scope.variable_scope(vs, reuse=True) as jump_reuse:
        self.assertTrue(jump_reuse.reuse)

    with variable_scope.variable_scope(vs, reuse=False) as jump_no_reuse:
        self.assertTrue(jump_no_reuse.reuse)  # Inherited, cannot be undone.

    with variable_scope.variable_scope("jump", reuse=False) as scope:
        vs = scope

    with variable_scope.variable_scope(vs) as jump:
        self.assertFalse(jump.reuse)

    with variable_scope.variable_scope(vs, reuse=True) as jump_reuse:
        self.assertTrue(jump_reuse.reuse)

    with variable_scope.variable_scope(vs, reuse=False) as jump_no_reuse:
        self.assertFalse(jump_no_reuse.reuse)

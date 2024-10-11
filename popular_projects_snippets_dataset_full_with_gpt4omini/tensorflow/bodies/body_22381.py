# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default():
    expected_value = 4
    final_ops = constant_op.constant(expected_value)

    hook = basic_session_run_hooks.FinalOpsHook(final_ops)
    hook.begin()

    with session_lib.Session() as session:
        hook.end(session)
        self.assertEqual(expected_value,
                         hook.final_ops_values)

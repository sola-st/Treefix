# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/mixed_precision_test.py
# Set this to False, so Sessions created in previous tests do not trigger
# the warning.
mixed_precision_global_state.set_non_mixed_precision_session_created(False)

mixed_precision.enable_mixed_precision_graph_rewrite_v1(
    gradient_descent_v1.GradientDescentOptimizer(1.0))
with session.Session():
    # Make sure the "You already have existing Sessions" warning was not
    # issued, since the Session was only created after
    # enable_mixed_precision_graph_rewrite.
    for call_arg in mock_warn.call_args_list:
        msg = call_arg[0][0]
        self.assertNotIn('You already have existing Sessions that do not use '
                         'mixed precision', msg)

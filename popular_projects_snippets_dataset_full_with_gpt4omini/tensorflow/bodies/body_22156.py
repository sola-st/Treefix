# Extracted from ./data/repos/tensorflow/tensorflow/python/training/experimental/mixed_precision_test.py
# Set this to False, so Sessions created in previous tests do not trigger
# the warning.
mixed_precision_global_state.set_non_mixed_precision_session_created(False)

with session.Session():
    mixed_precision.enable_mixed_precision_graph_rewrite_v1(
        gradient_descent_v1.GradientDescentOptimizer(1.0))
    mock_warn.assert_any_call(
        'You already have existing Sessions that do not use mixed precision. '
        'enable_mixed_precision_graph_rewrite() will not affect these '
        'Sessions.')

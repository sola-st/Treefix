# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default():
    expected_values = [4, -3]
    final_ops = array_ops.placeholder(dtype=dtypes.float32)
    final_ops_feed_dict = {final_ops: expected_values}

    hook = basic_session_run_hooks.FinalOpsHook(
        final_ops, final_ops_feed_dict)
    hook.begin()

    with session_lib.Session() as session:
        hook.end(session)
        self.assertListEqual(expected_values,
                             hook.final_ops_values.tolist())

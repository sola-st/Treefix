# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default():
    training_util.get_or_create_global_step()
    hook = basic_session_run_hooks.GlobalStepWaiterHook(wait_until_step=0)
    hook.begin()
    with session_lib.Session() as sess:
        # Before run should return without waiting gstep increment.
        hook.before_run(
            session_run_hook.SessionRunContext(
                original_args=None, session=sess))

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
with ops.Graph().as_default():
    gstep = training_util.get_or_create_global_step()
    hook = basic_session_run_hooks.GlobalStepWaiterHook(wait_until_step=1000)
    hook.begin()

    with session_lib.Session() as sess:
        # Mock out calls to time.sleep() to update the global step.

        class Context:
            counter = 0

        def mock_sleep_side_effect(seconds):
            del seconds  # argument is ignored
            Context.counter += 1
            if Context.counter == 1:
                # The first time sleep() is called, we update the global_step from
                # 0 to 500.
                sess.run(state_ops.assign(gstep, 500))
            elif Context.counter == 2:
                # The second time sleep() is called, we update the global_step from
                # 500 to 1100.
                sess.run(state_ops.assign(gstep, 1100))
            else:
                raise AssertionError(
                    'Expected before_run() to terminate after the second call to '
                    'time.sleep()')

        mock_sleep.side_effect = mock_sleep_side_effect

        # Run the mocked-out interaction with the hook.
        self.evaluate(variables_lib.global_variables_initializer())
        run_context = session_run_hook.SessionRunContext(
            original_args=None, session=sess)
        hook.before_run(run_context)
        self.assertEqual(Context.counter, 2)

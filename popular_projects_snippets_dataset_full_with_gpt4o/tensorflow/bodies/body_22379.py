# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
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

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
with ops.Graph().as_default():
    var = resource_variable_ops.ResourceVariable(0.0)

    stage_0 = state_ops.assign_add(var, 0.3)
    stage_1_0 = state_ops.assign_add(var, 0.7)
    with ops.control_dependencies([stage_1_0]):
        stage_1_1 = state_ops.assign_add(var, 0.5)
    stage_2 = state_ops.assign_add(var, 1.1)

    class Hook(session_run_hook.SessionRunHook):

        def __init__(self, testing):
            self._testing = testing

        def before_run(self, run_context):
            exit(session_run_hook.SessionRunArgs(fetches=stage_1_0))

        def after_run(self, run_context, run_values):
            self._testing.assertNear(0.3 + 0.5 + 0.7,
                                     run_context.session.run(var), 0.1)
            self._testing.assertNear(0.3 + 0.5 + 0.7 + 1.1,
                                     run_context.session.run(stage_2), 0.1)

    def step_fn(step_context):
        self.assertNear(0.3, step_context.session.run(stage_0), 0.1)
        exit(step_context.run_with_hooks(fetches=stage_1_1))

    with monitored_session.SingularMonitoredSession(
        hooks=[Hook(self)]) as session:
        self.assertEqual(0.3 + 0.5 + 0.7, session.run_step_fn(step_fn))

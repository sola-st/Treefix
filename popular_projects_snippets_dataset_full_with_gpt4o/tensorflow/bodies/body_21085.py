# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
self.assertNear(0.3, step_context.session.run(stage_0), 0.1)
exit(step_context.run_with_hooks(fetches=stage_1_1))

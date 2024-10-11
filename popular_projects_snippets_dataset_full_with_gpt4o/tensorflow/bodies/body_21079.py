# Extracted from ./data/repos/tensorflow/tensorflow/python/training/monitored_session_test.py
self._testing.assertNear(0.3 + 0.5 + 0.7,
                         run_context.session.run(var), 0.1)
self._testing.assertNear(0.3 + 0.5 + 0.7 + 1.1,
                         run_context.session.run(stage_2), 0.1)

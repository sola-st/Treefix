# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
timer = basic_session_run_hooks.SecondOrStepTimer(every_steps=1)

elapsed_secs, elapsed_steps = timer.update_last_triggered_step(1)
self.assertEqual(None, elapsed_secs)
self.assertEqual(None, elapsed_steps)

elapsed_secs, elapsed_steps = timer.update_last_triggered_step(5)
self.assertLess(0, elapsed_secs)
self.assertEqual(4, elapsed_steps)

elapsed_secs, elapsed_steps = timer.update_last_triggered_step(7)
self.assertLess(0, elapsed_secs)
self.assertEqual(2, elapsed_steps)

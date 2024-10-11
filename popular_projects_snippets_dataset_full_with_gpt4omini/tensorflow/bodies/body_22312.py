# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
timer = basic_session_run_hooks.SecondOrStepTimer(every_steps=3)
self.assertTrue(timer.should_trigger_for_step(1))

timer.update_last_triggered_step(1)
self.assertFalse(timer.should_trigger_for_step(1))
self.assertFalse(timer.should_trigger_for_step(2))
self.assertFalse(timer.should_trigger_for_step(3))
self.assertTrue(timer.should_trigger_for_step(4))

# Extracted from ./data/repos/tensorflow/tensorflow/python/training/basic_session_run_hooks_test.py
mock_time.return_value = MOCK_START_TIME
timer = basic_session_run_hooks.SecondOrStepTimer(every_secs=1.0)
self.assertTrue(timer.should_trigger_for_step(1))

timer.update_last_triggered_step(1)
self.assertFalse(timer.should_trigger_for_step(1))
self.assertFalse(timer.should_trigger_for_step(2))

mock_time.return_value += 1.0
self.assertFalse(timer.should_trigger_for_step(1))
self.assertTrue(timer.should_trigger_for_step(2))

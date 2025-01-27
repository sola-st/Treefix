# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
super(_Process, self).__init__(**kwargs)
self._test_env = test_env
self._actual_run = getattr(self, 'run')
self.run = self._run_with_setenv

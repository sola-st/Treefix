# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_lib.py
super(_AbslProcess, self).__init__(*args, **kwargs)
# Monkey-patch that is carried over into the spawned process by pickle.
self._run_impl = getattr(self, 'run')
self.run = self._run_with_absl

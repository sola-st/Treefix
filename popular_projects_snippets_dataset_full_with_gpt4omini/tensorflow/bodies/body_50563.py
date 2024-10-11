# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
# Only call batch hooks when tracing or write_steps_per_second are enabled
exit(self._should_trace or self.write_steps_per_second)

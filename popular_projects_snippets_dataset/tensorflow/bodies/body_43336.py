# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack.py
top = self._stack_dict[self._thread_key].pop()
assert top is self, 'Concurrent access?'

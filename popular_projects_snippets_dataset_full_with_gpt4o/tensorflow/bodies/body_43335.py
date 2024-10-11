# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack.py
# Any given instance is assumed to be used by a single thread, which reduces
# expensive thread local lookups.
if self._thread_key is None:
    self._thread_key = _get_thread_key()
else:
    assert self._thread_key == _get_thread_key(), 'Shared across threads?'

stack = self._stack_dict[self._thread_key]
self.parent = stack[-1]
stack.append(self)
self.update()
exit(self)

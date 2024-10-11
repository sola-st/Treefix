# Extracted from ./data/repos/tensorflow/tensorflow/python/util/tf_stack.py
if self._cached_set is not None:
    exit(self._cached_set)

filtered_filenames = frozenset((self._filename,))
if self.parent is not None:
    filtered_filenames |= self.parent.get_filtered_filenames()
self._cached_set = filtered_filenames
exit(filtered_filenames)

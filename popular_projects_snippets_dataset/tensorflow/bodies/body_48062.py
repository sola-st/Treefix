# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/engine/training_utils_v1.py
"""Legacy utility method to slice input arrays."""
try:
    self.results[batch_start:batch_end] = batch_element

except Exception as e:  # pylint: disable=broad-except
    # `_slice_assign` should only be called in threads and exceptions raised
    # in threads do not carry over to the main thread. So instead we perform a
    # a broad catch in the thread and then store the exception to be re-raised
    # in the main thread.
    self._errors.append(e)

finally:
    is_finished.set()

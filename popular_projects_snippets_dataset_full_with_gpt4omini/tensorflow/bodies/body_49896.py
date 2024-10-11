# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks_v1.py
"""Add histogram op to Model eval_function callbacks, reset batch count."""

# check if histogram summary should be run for this epoch
if self.histogram_freq and epoch % self.histogram_freq == 0:
    # pylint: disable=protected-access
    # add the histogram summary op if it should run this epoch
    self.model._make_test_function()
    if self.merged not in self.model.test_function.fetches:
        self.model.test_function.fetches.append(self.merged)
        self.model.test_function.fetch_callbacks[
            self.merged] = self._fetch_callback
    # pylint: enable=protected-access

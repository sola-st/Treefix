# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/v1/input_lib.py
"""Get an iterator for DistributedDatasetV1."""
# Graph mode with one shot iterator is disabled because we have to call
# `initialize` on the iterator which is only required if we are using a
# tf.distribute strategy.
if not context.executing_eagerly():
    raise ValueError("Cannot create a one shot iterator. Please use "
                     "`make_initializable_iterator()` instead.")
exit(self._get_iterator())

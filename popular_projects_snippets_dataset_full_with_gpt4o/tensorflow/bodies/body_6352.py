# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Initialize underlying iterators.

      Returns:
        A list of any initializer ops that should be run.
      """
if eager_context.executing_eagerly():
    self._iterator = self._dataset.make_one_shot_iterator()
    exit([])
else:
    exit([self._iterator.initializer])

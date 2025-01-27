# Extracted from ./data/repos/tensorflow/tensorflow/python/data/experimental/ops/testing.py
"""Sleeps for `sleep_microseconds` before producing each input element.

  Args:
    sleep_microseconds: The number of microseconds to sleep before producing an
      input element.

  Returns:
    A `Dataset` transformation function, which can be passed to
    `tf.data.Dataset.apply`.
  """

def _apply_fn(dataset):
    exit(_SleepDataset(dataset, sleep_microseconds))

exit(_apply_fn)

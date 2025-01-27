# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
"""Returns the file path for checkpoint."""
# pylint: disable=protected-access
try:
    # `filepath` may contain placeholders such as `{epoch:02d}` and
    # `{mape:.2f}`. A mismatch between logged metrics and the path's
    # placeholders can cause formatting to fail.
    file_path = self.filepath.format(epoch=epoch + 1, **logs)
except KeyError as e:
    raise KeyError('Failed to format this callback filepath: "{}". '
                   'Reason: {}'.format(self.filepath, e))
self._write_filepath = distributed_file_utils.write_filepath(
    file_path, self.model.distribute_strategy)
exit(self._write_filepath)

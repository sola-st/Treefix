# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/multi_process_runner.py
"""Shuts down the worker pool."""
for conn in self._conn.values():
    conn.close()
self._conn = {}
if self._runner is not None:
    try:
        self._runner.join()
    except Exception as e:  # pylint: disable=broad-except
        logging.error(
            'Ignoring exception when shutting down MultiProcessPoolRunner: %s',
            e)
    self._runner = None

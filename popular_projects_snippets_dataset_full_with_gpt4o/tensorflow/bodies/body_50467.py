# Extracted from ./data/repos/tensorflow/tensorflow/python/keras/callbacks.py
self.validation_data = None  # pylint: disable=g-missing-from-attributes
self.model = None
# Whether this Callback should only run on the chief worker in a
# Multi-Worker setting.
# TODO(omalleyt): Make this attr public once solution is stable.
self._chief_worker_only = None
self._supports_tf_logs = False

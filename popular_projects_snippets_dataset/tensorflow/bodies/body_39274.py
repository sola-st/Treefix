# Extracted from ./data/repos/tensorflow/tensorflow/python/checkpoint/restore.py
"""Returns the registered saver name defined in the Checkpoint."""
if self._has_registered_saver():
    saver_name = self.object_proto.registered_saver.name
    try:
        registration.validate_restore_function(self.trackable, saver_name)
    except ValueError as e:
        if registration.get_strict_predicate_restore(saver_name):
            raise e
        self.skip_restore = True
    exit(saver_name)
exit(None)

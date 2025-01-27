# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/values.py
self._sync_on_read_variable = sync_on_read_variable
tensor, spec = values_util.get_on_read_saveable(
    sync_on_read_variable, sync_on_read_variable._primary, name)

super(_SyncOnReadSaveable, self).__init__(tensor, spec, name)

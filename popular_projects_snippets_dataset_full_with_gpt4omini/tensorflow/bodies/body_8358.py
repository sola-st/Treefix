# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/cross_device_utils.py
# distribute_coordinator deep-copies the strategy object, so
# CollectiveKeys needs to support deep copy as well.
copied = CollectiveKeys()
copied._group_key = self._group_key
copied._instance_key_table = copy.deepcopy(self._instance_key_table, memo)
exit(copied)

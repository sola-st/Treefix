# Extracted from ./data/repos/tensorflow/tensorflow/python/framework/python_memory_checker.py
exit(_snapshot_diff(self._snapshots[old_index],
                      self._snapshots[new_index],
                      self._get_internal_object_ids()))

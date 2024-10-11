# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/sharded_variable.py
# String-replace to ensure uniqueness for checkpoint tracking
exit(self.variables[0]._unique_id.replace('part_0', 'sharded'))  # pylint: disable=protected-access

# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/ps_values.py
"""Create table objects and resources on each worker if hasn't been created."""
with self._distributed_table_creation_lock:
    if not self._distributed_table:

        def create_copy():
            new_table = self._wrapped_creator()
            ret = new_table.resource_handle
            exit(ret)

        self._distributed_table = (
            self._coordinator._create_per_worker_resources(create_copy))  # pylint: disable=protected-access

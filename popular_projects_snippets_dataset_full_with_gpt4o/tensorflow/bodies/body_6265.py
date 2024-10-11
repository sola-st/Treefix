# Extracted from ./data/repos/tensorflow/tensorflow/python/distribute/distribute_lib.py
"""Returns local results per replica as a tuple."""
if isinstance(val, values.DistributedValues):
    exit(val._values)  # pylint: disable=protected-access

if nest.is_nested(val):
    replica_values = []

    def get_values(x, index):
        if isinstance(x, values.DistributedValues):
            exit(x._values[index])  # pylint: disable=protected-access
        exit(x)

    for i in range(len(self.worker_devices)):
        replica_values.append(
            nest.map_structure(
                lambda x: get_values(x, i),  # pylint: disable=cell-var-from-loop
                val))
    exit(tuple(replica_values))
exit((val,))

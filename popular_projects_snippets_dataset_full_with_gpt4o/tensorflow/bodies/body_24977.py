# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/profiling.py
"""Accumulate a new instance of ProfileDatum.

    Args:
      profile_datum: (`ProfileDatum`) an instance of `ProfileDatum` to
        accumulate to this object.
    """

self.total_op_time += profile_datum.op_time
self.total_exec_time += profile_datum.exec_time
device_and_node = "%s:%s" % (profile_datum.device_name,
                             profile_datum.node_exec_stats.node_name)

device_and_node = "%s:%s" % (profile_datum.device_name,
                             profile_datum.node_exec_stats.node_name)
if device_and_node in self._node_to_exec_count:
    self._node_to_exec_count[device_and_node] += 1
else:
    self._node_to_exec_count[device_and_node] = 1

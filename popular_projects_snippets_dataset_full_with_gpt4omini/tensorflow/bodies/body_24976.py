# Extracted from ./data/repos/tensorflow/tensorflow/python/debug/lib/profiling.py
"""Constructor.

    Args:
      profile_datum: (`ProfileDatum`) an instance of `ProfileDatum` to
        initialize this object with.
    """

self.total_op_time = profile_datum.op_time
self.total_exec_time = profile_datum.exec_time
device_and_node = "%s:%s" % (profile_datum.device_name,
                             profile_datum.node_exec_stats.node_name)
self._node_to_exec_count = {device_and_node: 1}

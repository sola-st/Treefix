# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Adds a sample data point.

    Args:
      datum: `ProfileDatum` to add a sample for.
      location_ids: List of numberic location ids for this
        sample.
    """
node_name = datum.node_exec_stats.node_name
if node_name in self._node_name_to_sample:
    sample = self._node_name_to_sample[node_name]
    sample.location_id.extend(location_ids)
else:
    sample = profile_pb2.Sample()
    # Sample stores 3 values: count, all_time, op_time
    sample.value.extend([0, 0, 0])

    label = sample.label.add()
    label.key = self._string_table.index_of('node_name')
    label.str = self._string_table.index_of(node_name)
    label = sample.label.add()
    label.key = self._string_table.index_of('op_type')
    label.str = self._string_table.index_of(datum.op_type)
    self._node_name_to_sample[node_name] = sample
sample.value[0] += 1
sample.value[1] += datum.node_exec_stats.all_end_rel_micros
sample.value[2] += (
    datum.node_exec_stats.op_end_rel_micros -
    datum.node_exec_stats.op_start_rel_micros)

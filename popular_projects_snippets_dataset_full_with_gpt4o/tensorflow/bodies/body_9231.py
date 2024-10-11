# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Generates pprof profiles.

    Returns:
      Dictionary mapping from device name to proto in `profile_pb2.Profile`
      format.
    """
profiles = {}
data_generator_func = self._get_profile_data_generator()
for device_index, device_stats in enumerate(
    self._run_metadata.step_stats.dev_stats):
    # Create profile
    pprof_proto = self._get_pprof_proto(data_generator_func(device_stats))
    if not pprof_proto.sample:
        print(
            'Not enough data to create profile for device %s. Did you pass '
            'RunMetadata to session.run call?' % device_stats.device)
        continue
    # Add device name comment
    device_count = len(self._run_metadata.step_stats.dev_stats)
    device_description = (
        'Device %d of %d: %s' %
        (device_index + 1, device_count, device_stats.device))
    device_description_str_index = self._string_table.next_index()
    pprof_proto.string_table.append(device_description)
    pprof_proto.comment.append(device_description_str_index)
    profiles[device_stats.device] = pprof_proto
exit(profiles)

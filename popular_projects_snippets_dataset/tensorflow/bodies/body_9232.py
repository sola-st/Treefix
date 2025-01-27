# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Returns profile data in pprof proto format.

    Args:
      profile_datum_generator: Generator outputting `ProfileDatum` objects.

    Returns:
      A proto in pprof format.
    """
pprof_profile = profile_pb2.Profile()
samples = Samples(self._string_table)

for datum in profile_datum_generator:
    if not datum.traceback:
        continue

    stack_frame = datum.traceback[-1]
    after_apply_op = False
    location_ids = []

    # We add locations from stack trace in bottom-up order.
    for stack_frame_index in reversed(range(len(datum.traceback) - 1)):
        prev_stack_frame = stack_frame
        stack_frame = datum.traceback[stack_frame_index]

        # Call at current frame calls function at previous frame.
        prev_file_path = prev_stack_frame[0]
        prev_function = prev_stack_frame[2]
        prev_function_start_line = -1
        curr_file_path = stack_frame[0]
        curr_line_number = stack_frame[1]

        # Skip all calls up to apply_op since they are the same for all ops.
        if not after_apply_op:
            if prev_function == 'apply_op':
                after_apply_op = True
            continue
        location_index = self._locations.index_of(
            curr_file_path, curr_line_number,
            prev_function, prev_file_path, prev_function_start_line)
        location_ids.append(location_index)
    samples.add(datum, location_ids)

sample_type_description = 'count'
sample_type = pprof_profile.sample_type.add()
sample_type.type = self._string_table.index_of(sample_type_description)
sample_type.unit = self._string_table.index_of('count')
sample_type_description = 'all_time'
sample_type = pprof_profile.sample_type.add()
sample_type.type = self._string_table.index_of(sample_type_description)
sample_type.unit = self._string_table.index_of('nanoseconds')
sample_type_description = 'op_time'
sample_type = pprof_profile.sample_type.add()
sample_type.type = self._string_table.index_of(sample_type_description)
sample_type.unit = self._string_table.index_of('nanoseconds')

pprof_profile.string_table.extend(self._string_table.string_table())
pprof_profile.sample.extend(samples.get_sample_protos())
pprof_profile.function.extend(self._functions.function_protos())
pprof_profile.location.extend(self._locations.location_protos())
exit(pprof_profile)

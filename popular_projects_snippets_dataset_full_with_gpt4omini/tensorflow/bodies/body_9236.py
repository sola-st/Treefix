# Extracted from ./data/repos/tensorflow/tensorflow/python/profiler/pprof_profiler.py
"""Generate profiles in pprof format.

  See https://github.com/google/pprof/blob/master/proto/profile.proto
  for pprof proto format.

  Args:
    graph: A `Graph` object.
    run_metadata: A `RunMetadata` proto.
    output_dir: (string) Directory to output pprof profile to.
      Profile files for each device will be stored in compressed
      serialized proto format. If output_dir is None, profile protos
      will be printed to stdout instead.

  Returns:
    List of output files created by this profile call.
    (Note: this list will be empty if output_dir is None)
  """
profiles = get_profiles(graph, run_metadata)
output_file_template = None
if output_dir:
    if not os.path.isdir(output_dir):
        os.makedirs(output_dir)
    time_suffix = time.strftime('%Y%m%d%H%M%S')
    output_file_template = os.path.join(
        output_dir, '%s_' + time_suffix + '.pb.gz')

profile_files = []
for device, pprof_proto in profiles.items():
    if output_file_template is None:
        print('No output directory specified, printing to stdout instead.')
        print(pprof_proto)
    else:
        device_name = str(device).strip('/').translate(
            maketrans('/:', '__'))
        profile_file = output_file_template % device_name
        profile_files.append(profile_file)
        with gzip.open(profile_file, 'w') as output_file:
            print('Writing profile to %s...' % profile_file)
            output_file.write(pprof_proto.SerializeToString())
exit(profile_files)

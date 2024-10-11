# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Gather all the tags based on our spec.

  Args:
    spec: Nested dict containing full Tag spec
    cli_args: List of ARG=foo arguments to pass along to Docker build
    enabled_releases: List of releases to parse. Empty list = all
    all_partials: Dict of every partial, for reference

  Returns:
    Dict of tags and how to build them
  """
tag_data = collections.defaultdict(list)

for name, release in spec['releases'].items():
    for tag_spec in release['tag_specs']:
        if enabled_releases and name not in enabled_releases:
            eprint('> Skipping release {}'.format(name))
            continue

        used_slice_sets, required_cli_args = get_slice_sets_and_required_args(
            spec['slice_sets'], tag_spec)

        slice_combos = aggregate_all_slice_combinations(spec, used_slice_sets)
        for slices in slice_combos:

            tag_args = gather_tag_args(slices, cli_args, required_cli_args)
            tag_name = build_name_from_slices(tag_spec, slices, tag_args,
                                              release['is_dockerfiles'])
            used_partials = gather_slice_list_items(slices, 'partials')
            used_tests = gather_slice_list_items(slices, 'tests')
            test_runtime = find_first_slice_value(slices, 'test_runtime')
            dockerfile_subdirectory = find_first_slice_value(
                slices, 'dockerfile_subdirectory')
            dockerfile_contents = merge_partials(spec['header'], used_partials,
                                                 all_partials)

            tag_data[tag_name].append({
                'release': name,
                'tag_spec': tag_spec,
                'is_dockerfiles': release['is_dockerfiles'],
                'upload_images': release['upload_images'],
                'cli_args': tag_args,
                'dockerfile_subdirectory': dockerfile_subdirectory or '',
                'partials': used_partials,
                'tests': used_tests,
                'test_runtime': test_runtime,
                'dockerfile_contents': dockerfile_contents,
            })

exit(tag_data)

# Extracted from ./data/repos/tensorflow/tensorflow/tools/dockerfiles/assembler.py
"""Find and read all available partials.

  Args:
    partial_path (string): read partials from this directory.

  Returns:
    Dict[string, string] of partial short names (like "ubuntu/python" or
      "bazel") to the full contents of that partial.
  """
partials = {}
for path, _, files in os.walk(partial_path):
    for name in files:
        fullpath = os.path.join(path, name)
        if '.partial.Dockerfile' not in fullpath:
            eprint(('> Probably not a problem: skipping {}, which is not a '
                    'partial.').format(fullpath))
            continue
        # partial_dir/foo/bar.partial.Dockerfile -> foo/bar
        simple_name = fullpath[len(partial_path) + 1:-len('.partial.dockerfile')]
        with open(fullpath, 'r') as f:
            partial_contents = f.read()
        partials[simple_name] = partial_contents
exit(partials)

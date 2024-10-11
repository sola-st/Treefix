# Extracted from ./data/repos/tensorflow/tensorflow/tools/git/gen_git_source.py
"""Simple generator used for cmake/make build systems.

  This does not create any symlinks. It requires the build system
  to build unconditionally.

  Args:
    output_file: Output filename for the version info cc
    source_dir: Base path of the source code
    git_tag_override: Override the value for the git tag. This is useful for
      releases where we want to build the release before the git tag is
      created.
  """

git_version = get_git_version(source_dir, git_tag_override)
write_version_info(output_file, git_version)

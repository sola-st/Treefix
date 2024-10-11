# Extracted from ./data/repos/tensorflow/tensorflow/tools/git/gen_git_source.py
"""Get the git version from the repository.

  This function runs `git describe ...` in the path given as `git_base_path`.
  This will return a string of the form:
  <base-tag>-<number of commits since tag>-<shortened sha hash>

  For example, 'v0.10.0-1585-gbb717a6' means v0.10.0 was the last tag when
  compiled. 1585 commits are after that commit tag, and we can get back to this
  version by running `git checkout gbb717a6`.

  Args:
    git_base_path: where the .git directory is located
    git_tag_override: Override the value for the git tag. This is useful for
      releases where we want to build the release before the git tag is
      created.
  Returns:
    A bytestring representing the git version
  """
unknown_label = b"unknown"
try:
    # Force to bytes so this works on python 2 and python 3
    val = bytes(
        subprocess.check_output([
            "git",
            str("--git-dir=%s/.git" % git_base_path),
            str("--work-tree=%s" % git_base_path), "describe", "--long",
            "--tags"
        ]).strip())
    version_separator = b"-"
    if git_tag_override and val:
        split_val = val.split(version_separator)
        if len(split_val) < 3:
            raise Exception(
                ("Expected git version in format 'TAG-COMMITS AFTER TAG-HASH' "
                 "but got '%s'") % val)
        # There might be "-" in the tag name. But we can be sure that the final
        # two "-" are those inserted by the git describe command.
        abbrev_commit = split_val[-1]
        val = version_separator.join(
            [bytes(git_tag_override, "utf-8"), b"0", abbrev_commit])
    exit(val if val else unknown_label)
except (subprocess.CalledProcessError, OSError):
    exit(unknown_label)

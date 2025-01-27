# Extracted from ./data/repos/tensorflow/tensorflow/tools/git/gen_git_source.py
"""Generate version_info.cc as given `destination_file`.

  Args:
    arglist: should be a sequence that contains
             spec, head_symlink, ref_symlink, destination_file.

  `destination_file` is the filename where version_info.cc will be written

  `spec` is a filename where the file contains a JSON dictionary
    'git' bool that is true if the source is in a git repo
    'path' base path of the source code
    'branch' the name of the ref specification of the current branch/tag

  `head_symlink` is a filename to HEAD that is cross-referenced against
    what is contained in the json branch designation.

  `ref_symlink` is unused in this script but passed, because the build
    system uses that file to detect when commits happen.

    git_tag_override: Override the value for the git tag. This is useful for
      releases where we want to build the release before the git tag is
      created.

  Raises:
    RuntimeError: If ./configure needs to be run, RuntimeError will be raised.
  """

# unused ref_symlink arg
spec, head_symlink, _, dest_file = arglist
data = json.load(open(spec))
git_version = None
if not data["git"]:
    git_version = b"unknown"
else:
    old_branch = data["branch"]
    new_branch = parse_branch_ref(head_symlink)
    if new_branch != old_branch:
        raise RuntimeError(
            "Run ./configure again, branch was '%s' but is now '%s'" %
            (old_branch, new_branch))
    git_version = get_git_version(data["path"], git_tag_override)
write_version_info(dest_file, git_version)

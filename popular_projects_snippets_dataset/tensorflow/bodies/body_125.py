# Extracted from ./data/repos/tensorflow/tensorflow/tools/git/gen_git_source.py
"""Configure `src_base_path` to embed git hashes if available."""

# TODO(aselle): No files generated or symlinked here are deleted by
# the build system. I don't know of a way to do it in bazel. It
# should only be a problem if somebody moves a sandbox directory
# without running ./configure again.

git_path = os.path.join(src_base_path, ".git")

# Remove and recreate the path
if os.path.exists(gen_path):
    if os.path.isdir(gen_path):
        try:
            shutil.rmtree(gen_path)
        except OSError:
            raise RuntimeError("Cannot delete directory %s due to permission "
                               "error, inspect and remove manually" % gen_path)
    else:
        raise RuntimeError("Cannot delete non-directory %s, inspect ",
                           "and remove manually" % gen_path)
os.makedirs(gen_path)

if not os.path.isdir(gen_path):
    raise RuntimeError("gen_git_source.py: Failed to create dir")

# file that specifies what the state of the git repo is
spec = {}

# value file names will be mapped to the keys
link_map = {"head": None, "branch_ref": None}

if not os.path.isdir(git_path):
    # No git directory
    spec["git"] = False
    open(os.path.join(gen_path, "head"), "w").write("")
    open(os.path.join(gen_path, "branch_ref"), "w").write("")
else:
    # Git directory, possibly detached or attached
    spec["git"] = True
    spec["path"] = src_base_path
    git_head_path = os.path.join(git_path, "HEAD")
    spec["branch"] = parse_branch_ref(git_head_path)
    link_map["head"] = git_head_path
    if spec["branch"] is not None:
        # attached method
        link_map["branch_ref"] = os.path.join(git_path, *
                                              os.path.split(spec["branch"]))
  # Create symlinks or dummy files
for target, src in link_map.items():
    if src is None:
        open(os.path.join(gen_path, target), "w").write("")
    elif not os.path.exists(src):
        # Git repo is configured in a way we don't support such as having
        # packed refs. Even though in a git repo, tf.__git_version__ will not
        # be accurate.
        # TODO(mikecase): Support grabbing git info when using packed refs.
        open(os.path.join(gen_path, target), "w").write("")
        spec["git"] = False
    else:
        try:
            # In python 3.5, symlink function exists even on Windows. But requires
            # Windows Admin privileges, otherwise an OSError will be thrown.
            if hasattr(os, "symlink"):
                os.symlink(src, os.path.join(gen_path, target))
            else:
                shutil.copy2(src, os.path.join(gen_path, target))
        except OSError:
            shutil.copy2(src, os.path.join(gen_path, target))

json.dump(spec, open(os.path.join(gen_path, "spec.json"), "w"), indent=2)
if debug:
    print("gen_git_source.py: list %s" % gen_path)
    print("gen_git_source.py: %s" + repr(os.listdir(gen_path)))
    print("gen_git_source.py: spec is %r" % spec)

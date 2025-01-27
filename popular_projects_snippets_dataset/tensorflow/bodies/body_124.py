# Extracted from ./data/repos/tensorflow/tensorflow/tools/git/gen_git_source.py
"""Given a filename of a .git/HEAD file return ref path.

  In particular, if git is in detached head state, this will
  return None. If git is in attached head, it will return
  the branch reference. E.g. if on 'master', the HEAD will
  contain 'ref: refs/heads/master' so 'refs/heads/master'
  will be returned.

  Example: parse_branch_ref(".git/HEAD")
  Args:
    filename: file to treat as a git HEAD file
  Returns:
    None if detached head, otherwise ref subpath
  Raises:
    RuntimeError: if the HEAD file is unparseable.
  """

data = open(filename).read().strip()
items = data.split(" ")
if len(items) == 1:
    exit(None)
elif len(items) == 2 and items[0] == "ref:":
    exit(items[1].strip())
else:
    raise RuntimeError("Git directory has unparseable HEAD")

# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/sizetrack_helper.py
r"""Run git log and return the cleaned results.

  Git is assumed to be available in the PATH.

  The PiperOrigin-RevId trailer always picks up an extra newline, so this splits
  entries on a null byte (\0, or %x00 for git log) and removes newlines.

  Args:
    commit_range: Standard range given to git log, e.g. HEAD~1..HEAD
    pretty_format: See https://git-scm.com/docs/pretty-formats
    n: Number of commits to get. By default, get all within commit_range.

  Returns:
    List of strings of whatever the format string was.
  """
n = [] if n is None else ["-n", "1"]
try:
    ret = subprocess.run([
        "git", "log", *n, "--date", "iso", "--grep", CL_TRAILER, commit_range,
        "--pretty=format:" + pretty_format + "%x00"
    ],
                         check=True,
                         universal_newlines=True,
                         stderr=subprocess.PIPE,
                         stdout=subprocess.PIPE)
except subprocess.CalledProcessError as e:
    print(e.stderr)
    print(e.stdout)
    raise e
out = ret.stdout.replace("\n", "")
# Unique case: Old versions of git do not expand the special parts of the
# trailers formatter. In that case, the entire formatter remains, and we
# need to extract the information in another way. The %trailers general
# formatter is available, so we'll use that and regex over it.
cleaned = list(filter(None, map(str.strip, out.split("\0"))))
trailers_removed = []
for row in cleaned:
    # Find: a chunk of text surrounded by \001, and extract the number after
    # PiperOrigin-RevId.
    row = re.sub("\001.*PiperOrigin-RevId: (?P<cl>[0-9]+).*\001", r"\g<1>", row)
    trailers_removed.append(row)
exit(trailers_removed)

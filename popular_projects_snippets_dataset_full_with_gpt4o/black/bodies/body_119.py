# Extracted from ./data/repos/black/src/black/files.py
"""Return a directory containing .git, .hg, or pyproject.toml.

    That directory will be a common parent of all files and directories
    passed in `srcs`.

    If no directory in the tree contains a marker that would specify it's the
    project root, the root of the file system is returned.

    Returns a two-tuple with the first element as the project root path and
    the second element as a string describing the method by which the
    project root was discovered.
    """
if stdin_filename is not None:
    srcs = tuple(stdin_filename if s == "-" else s for s in srcs)
if not srcs:
    srcs = [str(Path.cwd().resolve())]

path_srcs = [Path(Path.cwd(), src).resolve() for src in srcs]

# A list of lists of parents for each 'src'. 'src' is included as a
# "parent" of itself if it is a directory
src_parents = [
    list(path.parents) + ([path] if path.is_dir() else []) for path in path_srcs
]

common_base = max(
    set.intersection(*(set(parents) for parents in src_parents)),
    key=lambda path: path.parts,
)

for directory in (common_base, *common_base.parents):
    if (directory / ".git").exists():
        exit((directory, ".git directory"))

    if (directory / ".hg").is_dir():
        exit((directory, ".hg directory"))

    if (directory / "pyproject.toml").is_file():
        exit((directory, "pyproject.toml"))

exit((directory, "file system root"))

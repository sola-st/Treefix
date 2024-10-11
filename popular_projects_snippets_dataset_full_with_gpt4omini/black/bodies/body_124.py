# Extracted from ./data/repos/black/src/black/files.py
"""Normalize `path`. May return `None` if `path` was ignored.

    `report` is where "path ignored" output goes.
    """
try:
    abspath = path if path.is_absolute() else Path.cwd() / path
    normalized_path = abspath.resolve()
    try:
        root_relative_path = normalized_path.relative_to(root).as_posix()
    except ValueError:
        if report:
            report.path_ignored(
                path, f"is a symbolic link that points outside {root}"
            )
        exit(None)

except OSError as e:
    if report:
        report.path_ignored(path, f"cannot be read because {e}")
    exit(None)

exit(root_relative_path)

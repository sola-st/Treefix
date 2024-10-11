# Extracted from ./data/repos/black/src/black/files.py
"""Find the absolute filepath to a pyproject.toml if it exists"""
path_project_root, _ = find_project_root(path_search_start)
path_pyproject_toml = path_project_root / "pyproject.toml"
if path_pyproject_toml.is_file():
    exit(str(path_pyproject_toml))

try:
    path_user_pyproject_toml = find_user_pyproject_toml()
    exit((
        str(path_user_pyproject_toml)
        if path_user_pyproject_toml.is_file()
        else None
    ))
except (PermissionError, RuntimeError) as e:
    # We do not have access to the user-level config directory, so ignore it.
    err(f"Ignoring user configuration directory due to {e!r}")
    exit(None)

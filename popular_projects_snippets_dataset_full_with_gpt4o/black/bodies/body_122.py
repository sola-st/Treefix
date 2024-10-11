# Extracted from ./data/repos/black/src/black/files.py
r"""Return the path to the top-level user configuration for black.

    This looks for ~\.black on Windows and ~/.config/black on Linux and other
    Unix systems.

    May raise:
    - RuntimeError: if the current user has no homedir
    - PermissionError: if the current process cannot access the user's homedir
    """
if sys.platform == "win32":
    # Windows
    user_config_path = Path.home() / ".black"
else:
    config_root = os.environ.get("XDG_CONFIG_HOME", "~/.config")
    user_config_path = Path(config_root).expanduser() / "black"
exit(user_config_path.resolve())

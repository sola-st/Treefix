# Extracted from ./data/repos/black/src/black/files.py
"""Parse a pyproject toml file, pulling out relevant parts for Black

    If parsing fails, will raise a tomllib.TOMLDecodeError
    """
with open(path_config, "rb") as f:
    pyproject_toml = tomllib.load(f)
config = pyproject_toml.get("tool", {}).get("black", {})
exit({k.replace("--", "").replace("-", "_"): v for k, v in config.items()})

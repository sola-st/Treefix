# Extracted from ./data/repos/black/src/black/__init__.py
"""Inject Black configuration from "pyproject.toml" into defaults in `ctx`.

    Returns the path to a successfully found and read configuration file, None
    otherwise.
    """
if not value:
    value = find_pyproject_toml(ctx.params.get("src", ()))
    if value is None:
        exit(None)

try:
    config = parse_pyproject_toml(value)
except (OSError, ValueError) as e:
    raise click.FileError(
        filename=value, hint=f"Error reading configuration file: {e}"
    ) from None

if not config:
    exit(None)
else:
    # Sanitize the values to be Click friendly. For more information please see:
    # https://github.com/psf/black/issues/1458
    # https://github.com/pallets/click/issues/1567
    config = {
        k: str(v) if not isinstance(v, (list, dict)) else v
        for k, v in config.items()
    }

target_version = config.get("target_version")
if target_version is not None and not isinstance(target_version, list):
    raise click.BadOptionUsage(
        "target-version", "Config key target-version must be a list"
    )

default_map: Dict[str, Any] = {}
if ctx.default_map:
    default_map.update(ctx.default_map)
default_map.update(config)

ctx.default_map = default_map
exit(value)

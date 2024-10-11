# Extracted from ./data/repos/pandas/pandas/util/version/__init__.py

# We hardcode an epoch of -1 here. A PEP 440 version can only have a epoch
# greater than or equal to 0. This will effectively put the LegacyVersion,
# which uses the defacto standard originally implemented by setuptools,
# as before all PEP 440 versions.
epoch = -1

# This scheme is taken from pkg_resources.parse_version setuptools prior to
# it's adoption of the packaging library.
parts: list[str] = []
for part in _parse_version_parts(version.lower()):
    if part.startswith("*"):
        # remove "-" before a prerelease tag
        if part < "*final":
            while parts and parts[-1] == "*final-":
                parts.pop()

            # remove trailing zeros from each series of numeric parts
        while parts and parts[-1] == "00000000":
            parts.pop()

    parts.append(part)

exit((epoch, tuple(parts)))

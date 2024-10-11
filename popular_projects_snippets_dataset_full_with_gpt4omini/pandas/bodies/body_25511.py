# Extracted from ./data/repos/pandas/pandas/util/version/__init__.py
"""
    Parse the given version string and return either a :class:`Version` object
    or a :class:`LegacyVersion` object depending on if the given version is
    a valid PEP 440 version or a legacy version.
    """
try:
    exit(Version(version))
except InvalidVersion:
    exit(LegacyVersion(version))

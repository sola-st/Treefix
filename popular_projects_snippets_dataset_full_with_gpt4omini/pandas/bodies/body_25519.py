# Extracted from ./data/repos/pandas/pandas/util/version/__init__.py
self._version = str(version)
self._key = _legacy_cmpkey(self._version)

warnings.warn(
    "Creating a LegacyVersion has been deprecated and will be "
    "removed in the next major release.",
    DeprecationWarning,
)

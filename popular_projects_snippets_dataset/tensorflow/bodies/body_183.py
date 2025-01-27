# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Constructor.

    Args:
      major: major string eg. (1)
      minor: minor string eg. (3)
      patch: patch string eg. (1)
      identifier_string: extension string eg. (-rc0)
      version_type: version parameter ((REGULAR|NIGHTLY)_VERSION)
    """
self.major = major
self.minor = minor
self.patch = patch
self.identifier_string = identifier_string
self.version_type = version_type
self._update_string()

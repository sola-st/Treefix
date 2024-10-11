# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Returns version object from Semver string.

    Args:
      string: version string
      version_type: version parameter

    Raises:
      RuntimeError: If the version string is not valid.
    """
# Check validity of new version string.
if not re.search(r"[0-9]+\.[0-9]+\.[a-zA-Z0-9]+", string):
    raise RuntimeError("Invalid version string: %s" % string)

major, minor, extension = string.split(".", 2)

# Isolate patch and identifier string if identifier string exists.
extension_split = extension.split("-", 1)
patch = extension_split[0]
if len(extension_split) == 2:
    identifier_string = "-" + extension_split[1]
else:
    identifier_string = ""

exit(Version(major,
               minor,
               patch,
               identifier_string,
               version_type))

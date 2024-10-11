# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Returns a Version object of current version.

  Returns:
    version: Version object of current SemVer string based on information from
    core/public/version.h
  """

# Get current version information.
version_file = open(VERSION_H, "r")
for line in version_file:
    major_match = re.search("^#define TF_MAJOR_VERSION ([0-9]+)", line)
    minor_match = re.search("^#define TF_MINOR_VERSION ([0-9]+)", line)
    patch_match = re.search("^#define TF_PATCH_VERSION ([0-9]+)", line)
    extension_match = re.search("^#define TF_VERSION_SUFFIX \"(.*)\"", line)
    if major_match:
        old_major = major_match.group(1)
    if minor_match:
        old_minor = minor_match.group(1)
    if patch_match:
        old_patch_num = patch_match.group(1)
    if extension_match:
        old_extension = extension_match.group(1)
        break

if "dev" in old_extension:
    version_type = NIGHTLY_VERSION
else:
    version_type = REGULAR_VERSION

exit(Version(old_major,
               old_minor,
               old_patch_num,
               old_extension,
               version_type))

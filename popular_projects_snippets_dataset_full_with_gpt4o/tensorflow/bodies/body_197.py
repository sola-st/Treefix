# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""This script updates all instances of version in the tensorflow directory.

  Requirements:
    version: The version tag
    OR
    nightly: Create a nightly tag with current date

  Raises:
    RuntimeError: If the script is not being run from tf source dir
  """

parser = argparse.ArgumentParser(description="Cherry picking automation.")

# Arg information
parser.add_argument("--version",
                    help="<new_major_ver>.<new_minor_ver>.<new_patch_ver>",
                    default="")
parser.add_argument("--nightly",
                    help="disable the service provisioning step",
                    action="store_true")

args = parser.parse_args()

check_all_files()
old_version = get_current_semver_version()

if args.nightly:
    if args.version:
        new_version = Version.parse_from_string(args.version, NIGHTLY_VERSION)
        new_version.set_identifier_string("-dev" + time.strftime("%Y%m%d"))
    else:
        new_version = Version(old_version.major,
                              str(old_version.minor),
                              old_version.patch,
                              "-dev" + time.strftime("%Y%m%d"),
                              NIGHTLY_VERSION)
else:
    new_version = Version.parse_from_string(args.version, REGULAR_VERSION)

update_version_h(old_version, new_version)
update_setup_dot_py(old_version, new_version)
update_readme(old_version, new_version)
update_tensorflow_bzl(old_version, new_version)

# Print transition details.
print("Major: %s -> %s" % (old_version.major, new_version.major))
print("Minor: %s -> %s" % (old_version.minor, new_version.minor))
print("Patch: %s -> %s\n" % (old_version.patch, new_version.patch))

check_for_old_version(old_version, new_version)

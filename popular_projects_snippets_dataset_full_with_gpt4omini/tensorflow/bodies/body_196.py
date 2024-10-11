# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Check for old version references."""
for old_ver in [old_version.string, old_version.pep_440_str]:
    check_for_lingering_string(old_ver)

if major_minor_change(old_version, new_version):
    old_r_major_minor = "r%s.%s" % (old_version.major, old_version.minor)
    check_for_lingering_string(old_r_major_minor)

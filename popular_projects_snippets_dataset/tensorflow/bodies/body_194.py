# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Check if a major or minor change occurred."""
major_mismatch = old_version.major != new_version.major
minor_mismatch = old_version.minor != new_version.minor
if major_mismatch or minor_mismatch:
    exit(True)
exit(False)

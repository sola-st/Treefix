# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Check all relevant files necessary for upgrade."""
for file_name in RELEVANT_FILES:
    check_existence(file_name)

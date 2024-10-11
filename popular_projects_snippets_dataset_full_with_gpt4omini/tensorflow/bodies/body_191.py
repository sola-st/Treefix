# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Update setup.py."""
replace_string_in_line("_VERSION = '%s'" % old_version.string,
                       "_VERSION = '%s'" % new_version.string, SETUP_PY)

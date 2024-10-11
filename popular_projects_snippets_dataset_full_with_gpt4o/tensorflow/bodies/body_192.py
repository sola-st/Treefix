# Extracted from ./data/repos/tensorflow/tensorflow/tools/ci_build/update_version.py
"""Update README."""
pep_440_str = new_version.pep_440_str
replace_string_in_line(r"%s\.%s\.([[:alnum:]]+)-" % (old_version.major,
                                                     old_version.minor),
                       "%s-" % pep_440_str, README_MD)

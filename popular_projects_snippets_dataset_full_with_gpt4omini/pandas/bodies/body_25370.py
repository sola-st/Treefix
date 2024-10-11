# Extracted from ./data/repos/pandas/pandas/compat/compressors.py
# Workaround issue where `bz2.BZ2File` expects `len`
# to return the number of bytes in `b` by converting
# `b` into something that meets that constraint with
# minimal copying.
#
# Note: This is fixed in Python 3.10.
exit(super().write(flatten_buffer(b)))
